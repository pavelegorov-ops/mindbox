---
title: Cинхронизация deviceUUID между React Native mobile SDK и JS SDK в приложении с WebView
slug: "sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview-react-native"
source_url: "https://developers.mindbox.ru/docs/sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview-react-native"
breadcrumb:
  - Мобильные приложения
  - React Native SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:0bba525fc79a85795c1b802d2ff6921d1f959051f01595ca632df14078fb8851"
---

# Cинхронизация deviceUUID между React Native mobile SDK и JS SDK в приложении с WebView

### Результат шага

- В административной панели mindbox создается 1 карточка клиента, в которую попадают действия и из мобильного SDK, и из JS SDK сайта.

[Пример реализации](https://github.com/mindbox-cloud/react-native-sdk/blob/webView_integration/example/exampleApp/src/screens/HomeScreen.tsx)

1. **Добавьте метод для получения deviceUUID**

```
// Установите приемлемый для вас тайм-аут ожидания deviceUUID
// Если не дождаться получения deviceUUID при первой инициализации,
// синхронизация произойдет при следующей загрузке страницы или запуске приложения.
// При использовании сторонних cookie на сайте обязательно дождитесь получения deviceUUID,
// иначе синхронизации не произойдет.

const MAX_UUID_WAIT_TIME = Platform.OS === 'ios' ? 250 : 4000;

// Функция ожидания получения deviceUUID в течение MAX_UUID_WAIT_TIME
const waitForDeviceUUID = (timeout) => {
  return new Promise((resolve, reject) => {
    const timeoutHandler = setTimeout(() => {
      console.log('Device UUID не получен в течение тайм-аута');
      reject(new Error('Device UUID не получен в течение тайм-аута'));
    }, timeout);

    MindboxSdk.getDeviceUUID((uuid) => {
      console.log('Получен Device UUID:', uuid);
      clearTimeout(timeoutHandler);
      if (uuid) {
        resolve(uuid);
      } else {
        reject(new Error('Device UUID пустой или неопределен'));
      }
    });
  });
};
```

### При первой инициализации mindbox SDK deviceUUID может быть получен от провайдера в течение нескольких секунд.

При следующих инициализациях deviceUUID будет получен в течение 100-200 мсек

### Использование third-party cookie

По умолчанию, начиная с Android API 21 и IOS 12, использование third-party cookies отключено.

При использовании third-party cookies, вам обязательно надо дождаться получения deviceUUID при первой инициализации.

2. **Добавьте код ожидания получения deviceUUID перед загрузкой страницы в useEffect**

```
useEffect(() => {
  // Пытаемся получить мобильный deviceUUID в течение указанного тайм-аута (MAX_UUID_WAIT_TIME).
  // Страница начнет загружаться либо сразу после получения UUID, либо после истечения тайм-аута.
  // Если UUID не может быть получен, синхронизация произойдет при следующей загрузке страницы или запуске приложения.
  const initialize = async () => {
    try {
      console.log('Начинаем waitForDeviceUUID...')
      const uuid = await waitForDeviceUUID(MAX_UUID_WAIT_TIME)
      setDeviceUUID(uuid)
      // Запускаем загрузку страницы
      setCanLoadWebView(true)
      console.log('Завершено waitForDeviceUUID, Device UUID:', uuid)
    } catch (error) {
      // Даже если получение deviceUUID превысило время ожидания во время первой загрузки страницы,
      // синхронизация произойдет при последующих загрузках страницы или запусках приложения.
      MindboxSdk.getDeviceUUID((uuid) => {
        setDeviceUUID(uuid)
        console.log('Device UUID получен после истечения тайм-аута:', uuid)
      })
      setCanLoadWebView(true)
    }
  }

  // Инициализируем Mindbox SDK
  const appInitializationCallback = async () => {
    try {
      await MindboxSdk.initialize(configuration)
    } catch (error) {
      console.log(error)
    }
  }
  appInitializationCallback()
  initialize()
}, [])
```

3. **Добавьте метод для синхронизации deviceUUID между мобильным SDK и JS SDK**

```
// Функция для синхронизации deviceUUID с JS SDK
const synchronizeDeviceUUID = (uuid) =>
`
  try {
    const deviceUUID = '${uuid || ''}';
    if (deviceUUID) {
      document.cookie = "mindboxDeviceUUID=" + deviceUUID;
      localStorage.setItem('mindboxDeviceUUID', deviceUUID);
      window.ReactNativeWebView.postMessage(JSON.stringify({ status: 'successSync' }));
    } else {
      window.ReactNativeWebView.postMessage(JSON.stringify({ status: 'errorSync', message: 'deviceUUID is null or undefined' }));
    }
  } catch (error) {
    window.ReactNativeWebView.postMessage(JSON.stringify({ status: 'errorSync', message: error.message }));
  }
`
```

4. **В компоненте WebView используйте метод synchronizeDeviceUUID**

```
return (
    <SafeAreaView style={styles.container}>
      {canLoadWebView ? (
        <>
          <WebView style={{ flex: 1 }} ref={webViewRef} source={{ uri: webViewUrl }} 
          javaScriptEnabled={true}
           domStorageEnabled={true} 
           injectedJavaScriptBeforeContentLoaded={synchronizeDeviceUUID(deviceUUID)} 
           onMessage={onMessage} />
          <View style={styles.buttonContainer}>
            <Button title="Show Data" onPress={showData} />
          View>
        
      ) : (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#0000ff" />
          <Text>Waiting for Device UUID...Text>
        View>
      )}
    </SafeAreaView>
  )
```

## Отладка

1. **В колбэке onMessage обработайте сообщения из WebView**

```
// Обработчик сообщений, полученных из WebView
const onMessage = (event) => {
  const data = JSON.parse(event.nativeEvent.data)
  // Используем оператор switch для обработки различных случаев
  switch (data.status) {
    case 'errorSync':
      console.error('Ошибка выполнения JavaScript:', data.message)
      break
    case 'successSync':
      console.log('Синхронизация успешна.')
      break
    default:
      if (data.cookies || data.deviceUUID) {
        console.log('Cookies:', data.cookies)
        console.log('Device UUID из JS SDK:', data.deviceUUID)
        console.log('Device UUID из мобильного SDK:', deviceUUID)
      } else if (data.error) {
        console.error('Ошибка из WebView:', data.error)
      } else {
        console.log('Необработанное сообщение:', data)
      }
      break
  }
}
```

2. **Добавьте метод для отладки синхронизации**

```
// Метод для отладки синхронизации.
// Отображает deviceUUID, хранящийся в cookies, localStorage, и мобильный deviceUUID.
// Эти значения deviceUUID должны совпадать. Вызывайте после загрузки страницы
const showData = () => {
  if (!webViewRef.current) {
    console.error('WebView не инициализирован.')
    return
  }
  const script = `
    (function() {
      try {
        const cookies = document.cookie || 'No cookies found';
        const deviceUUID = localStorage.getItem('mindboxDeviceUUID') || 'No deviceUUID found';
        window.ReactNativeWebView.postMessage(JSON.stringify({
          cookies,
          deviceUUID
        }));
      } catch (error) {
        window.ReactNativeWebView.postMessage(JSON.stringify({ error: error.message }));
      }
    })();
  `
  webViewRef.current.injectJavaScript(script)
}
```

## Пример готового файла

```
import React, { useEffect, useState, useRef } from 'react'
import { SafeAreaView, StyleSheet, Text, View, Button, ActivityIndicator, Platform } from 'react-native'
import MindboxSdk, { LogLevel } from 'mindbox-sdk'
import { WebView } from 'react-native-webview'

// Configuration for Mindbox SDK initialization
const configuration = {
  domain: 'api.mindbox.ru',
  endpointId: Platform.OS === 'ios' ? 'your-ios-endpoint-system-name' : 'your-android-endpoint-system-name',
  subscribeCustomerIfCreated: true,
  shouldCreateCustomer: true,
}

// Timeout for waiting to fetch the deviceUUID.
// The page will not start loading until this timeout expires.
// During the first initialization on Android, fetching may take a few seconds,
// while subsequent attempts typically take less than 250 ms.
const MAX_UUID_WAIT_TIME = Platform.OS === 'ios' ? 250 : 4000

const HomeScreen = () => {
  const [deviceUUID, setDeviceUUID] = useState(null)
  const [canLoadWebView, setCanLoadWebView] = useState(false)
  const webViewRef = useRef(null)
  const webViewUrl = 'https://example.com'

  // Function to synchronize deviceUUID with the JS SDK
  const synchronizeDeviceUUID = (uuid) => `
    try {
      const deviceUUID = '${uuid || ''}';
      if (deviceUUID) {
        document.cookie = "mindboxDeviceUUID=" + deviceUUID;
        localStorage.setItem('mindboxDeviceUUID', deviceUUID);
        window.ReactNativeWebView.postMessage(JSON.stringify({ status: 'successSync' }));
      } else {
        window.ReactNativeWebView.postMessage(JSON.stringify({ status: 'errorSync', message: 'deviceUUID is null or undefined' }));
      }
    } catch (error) {
      window.ReactNativeWebView.postMessage(JSON.stringify({ status: 'errorSync', message: error.message }));
    }
  `

  // Handler for messages received from the WebView
  const onMessage = (event) => {
    const data = JSON.parse(event.nativeEvent.data)
    // Using switch statement to handle different cases
    switch (data.status) {
      case 'errorSync':
        console.error('JavaScript execution error:', data.message)
        break
      case 'successSync':
        console.log('Synchronization successful.')
        break
      default:
        if (data.cookies || data.deviceUUID) {
          console.log('Cookies:', data.cookies)
          console.log('Device UUID from JS SDK:', data.deviceUUID)
          console.log('Device UUID from mobile SDK:', deviceUUID)
        } else if (data.error) {
          console.error('Error from WebView:', data.error)
        } else {
          console.log('Unhandled message:', data)
        }
        break
    }
  }

  // Debugging method for synchronization.
  // Displays the deviceUUID stored in cookies, localStorage, and the mobile device UUID.
  // These values of deviceUUID should match.
  const showData = () => {
    if (!webViewRef.current) {
      console.error('WebView is not initialized.')
      return
    }
    const script = `
      (function() {
        try {
          const cookies = document.cookie || 'No cookies found';
          const deviceUUID = localStorage.getItem('mindboxDeviceUUID') || 'No deviceUUID found';
          window.ReactNativeWebView.postMessage(JSON.stringify({
            cookies,
            deviceUUID
          }));
        } catch (error) {
          window.ReactNativeWebView.postMessage(JSON.stringify({ error: error.message }));
        }
      })();
    `
    webViewRef.current.injectJavaScript(script)
  }

  useEffect(() => {
    // Attempts to fetch the mobile device UUID within the specified timeout (MAX_UUID_WAIT_TIME).
    // The page will start loading either as soon as the UUID is fetched or after the timeout expires.
    // If the UUID cannot be fetched, synchronization will happen on the next page load or app launch.
    const initialize = async () => {
      try {
        console.log('Starting waitForDeviceUUID...')
        const uuid = await waitForDeviceUUID(MAX_UUID_WAIT_TIME)
        setDeviceUUID(uuid)
        setCanLoadWebView(true)
        console.log('Finished waitForDeviceUUID, Device UUID:', uuid)
      } catch (error) {
        // Even if fetching the deviceUUID times out during the initial page load,
        // synchronization will occur on subsequent page loads or app launches.
        MindboxSdk.getDeviceUUID((uuid) => {
          setDeviceUUID(uuid)
          console.log('Device UUID received after timeout:', uuid)
        })
        setCanLoadWebView(true)
      }
    }

    // Initialize the Mindbox SDK
    const appInitializationCallback = async () => {
      try {
        await MindboxSdk.initialize(configuration)
      } catch (error) {
        console.log(error)
      }
    }

    appInitializationCallback()
    initialize()
    MindboxSdk.setLogLevel(LogLevel.DEBUG)
    MindboxSdk.getToken((token) => {
      console.log('Token:', token)
    })
    MindboxSdk.getSdkVersion((version) => {
      console.log('Sdk version:', version)
    })
  }, [])

  // Fetches the deviceUUID within the specified timeout period.
  // Note: The MAX_UUID_WAIT_TIME should not be set to less than 250 ms,
  // as the deviceUUID might not be fetched in time.
  const waitForDeviceUUID = (timeout) => {
    return new Promise((resolve, reject) => {
      const timeoutHandler = setTimeout(() => {
        console.log('Device UUID not received within timeout')
        reject(new Error('Device UUID not received within timeout'))
      }, timeout)

      MindboxSdk.getDeviceUUID((uuid) => {
        console.log('Device UUID received:', uuid)
        clearTimeout(timeoutHandler)
        resolve(uuid)
      })
    })
  }

  return (
    <SafeAreaView style={styles.container}>
      {canLoadWebView ? (
        <>
          <WebView style={{ flex: 1 }} ref={webViewRef} source={{ uri: webViewUrl }}
          javaScriptEnabled={true}
           domStorageEnabled={true}
           injectedJavaScriptBeforeContentLoaded={synchronizeDeviceUUID(deviceUUID)}
           onMessage={onMessage} />
          <View style={styles.buttonContainer}>
            <Button title="Show Data" onPress={showData} />
          View>
        
      ) : (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#0000ff" />
          <Text>Waiting for Device UUID...Text>
        View>
      )}
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonContainer: {
    padding: 10,
    backgroundColor: '#f0f0f0',
  },
})

export default HomeScreen
```
