---
title: Cинхронизация deviceUUID между Android mobile SDK и JS SDK в приложении с WebView
slug: "sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview"
source_url: "https://developers.mindbox.ru/docs/sync-deviceuuid-between-mobile-sdk-and-js-sdk-webview"
breadcrumb:
  - Мобильные приложения
  - Android SDK
fetched_at: "2026-05-13T11:53:23Z"
content_hash: "sha256:dc15a4ca045962516807c47c011888374bfc8a4b8751b899b6af12e609618f6a"
---

# Cинхронизация deviceUUID между Android mobile SDK и JS SDK в приложении с WebView

### Результат шага

В административной панели mindbox создается 1 карточка клиента, в которую попадают действия и из мобильного SDK, и из JS SDK сайта.

[Пример реализации](https://github.com/mindbox-cloud/android-sdk/blob/webView_integration/example/app/src/main/java/com/mindbox/example/MainActivity.kt)

Если ваше приложение с WebView, на нем может работать [JS трекер сайта](javascript-sdk.md). Поэтому при установке моб. приложения, в mindbox будет создаваться по 2 карточки одного и того же клиента с разными deviceUUID: из JS SDK и из mobile SDK. Чтобы этого избежать и хранить все данные в 1 карточке клиента, выполните действия по инструкции:

1. **Добавьте в приложение метод по получению deviceUUID**

```
companion object {
    // Установите приемлемый для вас тайм-аут ожидания deviceUUID
    // Если не дождаться получения deviceUUID при первой инициализации, 
    // синхронизация произойдет при следующей загрузке страницы / запуске приложения
    // При использовании third-party cookies на сайте, обязательно дождитесь получения deviceUUID
    // иначе синхронизации не произойдет
    const val FETCHING_DEVICE_UUID_TIMEOUT = 5000L // в миллисекундах
}

// Метод будет ожидать получение deviceUUID в течении FETCHING_DEVICE_UUID_TIMEOUT
private suspend fun getDeviceUUID(): String = withTimeout(FETCHING_DEVICE_UUID_TIMEOUT) {
    suspendCancellableCoroutine { continuation ->
        Mindbox.subscribeDeviceUuid { uuid ->
            if (uuid.isNotEmpty()) {
                continuation.resume(uuid)
            } else {
                continuation.resumeWithException(Exception("Device UUID is empty"))
            }
        }
    }
}
```

### При первой инициализации mindbox SDK deviceUUID может быть получен от провайдера в течение нескольких секунд.

При следующих инициализациях deviceUUID будет получен в течение 100-200 мсек

### Про использование third-party cookies:

По умолчанию, начиная с Android API 21, использование third-party cookies отключено. Убедитесь, что у вас не вызывается метод `CookieManager.getInstance().setAcceptThirdPartyCookies(webView, true)`, если вам не требуется использовать third-party cookies.

При использовании third-party cookies, вам обязательно надо дождаться получения deviceUUID при первой инициализации.

2. **Добавьте код ожидания получения deviceUUID перед загрузкой страницы в методе onCreate MainActivity**

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Инициализация вашего WebView и других компонентов

    // Запуск корутины для ожидания deviceUUID перед загрузкой страницы
    CoroutineScope(Dispatchers.Main).launch {
        try {
						// вызываем получение deviceUUID не блокируя main поток
            	deviceUUID = withContext(Dispatchers.IO) {
                getDeviceUUID()
            }
            Mindbox.writeLog("DeviceUUID для синхронизации получен: $deviceUUID", logLevel = Level.DEBUG)
            webView.loadUrl(URL)
        } catch (e: TimeoutCancellationException) {
            Mindbox.writeLog("Превышено время ожидания получения Device UUID. Загрузка без UUID", logLevel = Level.DEBUG)
            webView.loadUrl(URL)
        } catch (e: Exception) {
            Mindbox.writeLog("Не удалось получить Device UUID для синхронизации: ${e.message}", logLevel = Level.ERROR)
            webView.loadUrl(URL)
        }
    }
 // Остальной код вашего метода onCreate
}
```

3. **Добавьте метод для синхронизации deviceUUID между mobile SDK и JS SDK**

```
// Этот метод передает deviceUUID в веб-страницу через куки и localStorage
private fun syncMindboxDeviceUUIDs(uuid: String) {
    webView.evaluateJavascript(
        """
        document.cookie = "mindboxDeviceUUID=$uuid";
        window.localStorage.setItem('mindboxDeviceUUID', '$uuid');
        """
    ) {
        Mindbox.writeLog("Device UUID синхронизирован: $uuid", logLevel = Level.DEBUG)
    }
}
```

4. **В колбеке onPageStarted WebViewClient вызовите метод syncMindboxDeviceUUIDs**

```
private val webViewClientInstance: WebViewClient by lazy {
    object : WebViewClient() {
        override fun onPageStarted(view: WebView, url: String?, favicon: android.graphics.Bitmap?) {
            super.onPageStarted(view, url, favicon)
            Log.d(Utils.TAG, "Начата загрузка страницы: $url")
            // Синхронизация deviceUUID
            deviceUUID?.let {
                syncMindboxDeviceUUIDs(it)
            } ?: run {
                Mindbox.subscribeDeviceUuid { uuid ->
                    if (uuid.isNotEmpty()) {
                        deviceUUID = uuid
                        syncMindboxDeviceUUIDs(uuid)
                    }
                }
            }
        }
    }
}
```

# Пример готового файла

```
package com.mindbox.example

import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.webkit.*
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import cloud.mindbox.mobile_sdk.Mindbox
import cloud.mindbox.mobile_sdk.logger.Level
import com.mindbox.example.databinding.ActivityMainBinding
import kotlinx.coroutines.*
import kotlin.coroutines.*

@RequiresApi(Build.VERSION_CODES.LOLLIPOP)
class MainActivity : AppCompatActivity() {

    companion object {
        const val URL = "https://your-website.com/"
        const val FETCHING_DEVICE_UUID_TIMEOUT = 4000L
    }

    private lateinit var webView: WebView
    private var deviceUUID: String? = null
    private var _binding: ActivityMainBinding? = null
    private val binding: ActivityMainBinding
        get() = _binding!!

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        _binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //Use this line to enable debugging
        WebView.setWebContentsDebuggingEnabled(true)

        //initialize webview after Mindbox.init if init in activity
        webView = binding.webView.apply {
            settings.javaScriptEnabled = true
            settings.domStorageEnabled = true
            webViewClient = webViewClientInstance
        }

        /***
         * Start loading the page after obtaining the deviceUUID.
         * On the first app launch, obtaining the deviceUUID may take several seconds.
         * If you don't wait for the deviceUUID, synchronization will occur on the next page load.
         * The waiting time can be adjusted in the GET_DEVICE_UUID_TIMEOUT constant.
         ***/
        CoroutineScope(Dispatchers.Main).launch {
            try {
                  deviceUUID = withContext(Dispatchers.IO) {
                    getDeviceUUID()
                }
                Mindbox.writeLog("DeviceUUID for synchronization received: $deviceUUID", logLevel = Level.DEBUG)
                webView.loadUrl(URL)
            } catch (e: TimeoutCancellationException) {
                Mindbox.writeLog("Timeout while waiting for synchronization Device UUID. Loading without UUID", logLevel = Level.DEBUG)
                webView.loadUrl(URL)
            } catch (e: Exception) {
                Mindbox.writeLog("Failed to get Device UUID for synchronization: ${e.message}", logLevel = Level.ERROR)
                webView.loadUrl(URL)
            }
        }

        binding.viewCookiesButton.setOnClickListener {
            showCookies()
        }

        processMindboxIntent(intent = intent, context = this)?.let { (url, payload) ->
            Log.d(Utils.TAG, "Data from push: url: $url, payload: $payload")
        }

    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        processMindboxIntent(intent = intent, context = this)?.let { (url, payload) ->
            Log.d(Utils.TAG, "Data from push: url: $url, payload: $payload")
        }
        Mindbox.onNewIntent(intent)
    }

    override fun onDestroy() {
        super.onDestroy()
        _binding = null
    }

    private val webViewClientInstance: WebViewClient by lazy {

        object : WebViewClient() {

            override fun onPageStarted(view: WebView, url: String?, favicon: android.graphics.Bitmap?) {
                super.onPageStarted(view, url, favicon)
                Log.d(Utils.TAG, "Page started loading: $url")
                // Synchronizing deviceUUID
                deviceUUID?.let {
                    syncMindboxDeviceUUIDs(it)
                } ?: run {
                    Mindbox.subscribeDeviceUuid { uuid ->
                        if (uuid.isNotEmpty()) {
                            deviceUUID = uuid
                            syncMindboxDeviceUUIDs(uuid)
                        }
                    }
                }
            }
        }
    }

    // Getting device UUID by mindbox mobile sdk
    private suspend fun getDeviceUUID(): String = withTimeout(FETCHING_DEVICE_UUID_TIMEOUT) {
        suspendCancellableCoroutine { continuation ->
            Mindbox.subscribeDeviceUuid { uuid ->
                if (uuid.isNotEmpty()) {
                    continuation.resume(uuid)
                } else {
                    continuation.resumeWithException(Exception("Device UUID is empty"))
                }
            }
        }
    }

    // Synchronize deviceUUID
    private fun syncMindboxDeviceUUIDs(uuid: String) {
        webView.evaluateJavascript(
            """
            document.cookie = "mindboxDeviceUUID=$uuid";
            window.localStorage.setItem('mindboxDeviceUUID', '$uuid');
            """
        ) {
            Mindbox.writeLog("Device UUID synchronized with deviceUUID: $uuid", logLevel = Level.DEBUG)
        }
    }

    // Use it to debug data after tracker initialize
    // For example add button for debug
    private fun showCookies() {
        val cookies = CookieManager.getInstance().getCookie(URL)
        Log.d(Utils.TAG, "Cookies: $cookies")
        Mindbox.subscribeDeviceUuid { uuid ->
            Log.d(Utils.TAG, "mobile sdk deviceUUID=$uuid")
        }
        webView.evaluateJavascript(
            "(function() {return window.localStorage.getItem('mindboxDeviceUUID')})()"
        ) { result ->
            Log.d(Utils.TAG, "js sdk deviceUUID: $result")
        }
    }

    // Use this method to clear WebView cache
    @RequiresApi(Build.VERSION_CODES.LOLLIPOP)
    private fun clearAllCookies() {

        WebStorage.getInstance().deleteAllData()
        val cookieManager = CookieManager.getInstance()
        cookieManager.removeAllCookies { success ->
            if (success) {
                Log.d(Utils.TAG, "All cookies cleared")
            } else {
                Log.e(Utils.TAG, "Failed to clear cookies")
            }
        }
    }
}
```

# Отладка

Для отладки можно использовать следующий метод. Он вернет mobile device UUID, deviceUUID в cookies и deviceUUID в LocalStorage. Все эти значения должны соответствовать друг другу.

Выполните этот метод после инициализации tracker js:

```
private fun showCookies() {
    val cookies = CookieManager.getInstance().getCookie(URL)
    Log.d(Utils.TAG, "Cookies: $cookies")
    Mindbox.subscribeDeviceUuid { uuid ->
        Log.d(Utils.TAG, "mobile sdk deviceUUID=$uuid")
    }
    webView.evaluateJavascript(
        "(function() { return window.localStorage.getItem('mindboxDeviceUUID'); })();"
    ) { result ->
        Log.d(Utils.TAG, "js sdk deviceUUID: $result")
    }
}
```
