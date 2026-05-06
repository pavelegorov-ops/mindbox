---
title: Cинхронизация deviceUUID между iOS mobile SDK и JS SDK в приложении с WebView
slug: "ios-webview-sync-with-sdk"
source_url: "https://developers.mindbox.ru/docs/ios-webview-sync-with-sdk"
breadcrumb:
  - Мобильные приложения
  - iOS SDK
fetched_at: "2026-05-04T14:26:15Z"
content_hash: "sha256:411a72fe59fc71b954452005eb55763a41c810b0e7f49f226021e24dc65b8218"
---

# Cинхронизация deviceUUID между iOS mobile SDK и JS SDK в приложении с WebView

### Результат шага:

- В административной панели Mindbox создается 1 карточка клиента, в которую попадают действия и из мобильного SDK, и с сайта использующего JS SDK.

[Пример реализации](https://github.com/mindbox-cloud/ios-sdk/blob/webView_integration/Example/Example/Views/WebView.swift)

Если ваше приложение использует WebView с сайтом на котором используется [JS трекер](javascript-sdk.md), при установке моб. приложения, в mindbox будет создаваться по 2 карточки одного и того же клиента с разными deviceUUID: одна из JS SDK и другая из mobile SDK. Чтобы этого избежать и хранить все данные в одной карточке клиента, нужно выполнить следующие действия:

1. **Добавьте в приложение код, который при получении deviceUUID из мобильного SDK, будет синхронизировать его с JS SDK**

```
func syncMindboxDeviceUUIDs(with webView: WKWebView) {
    Mindbox.shared.getDeviceUUID { uuid in
        guard !uuid.isEmpty else {
            Mindbox.logger.log(level: .error, message: "[WebView]: Device UUID is empty or invalid")
            return
        }

        let script = """
            document.cookie = "mindboxDeviceUUID=\(uuid); path=/";
            window.localStorage.setItem('mindboxDeviceUUID', '\(uuid)');
        """

        DispatchQueue.main.async {
            webView.evaluateJavaScript(script) { _, error in
                if let error = error {
                    Mindbox.logger.log(level: .error, message: "[WebView]: Error setting cookies and localStorage: \(error)")
                } else {
                    Mindbox.logger.log(level: .default, message: "[WebView]: Cookies and localStorage set successfully.")
                }
            }
        }
    }
}
```

2. **Вызовите этот метод в`webView(_:didCommit:)` при реализации `WKNavigationDelegate` вашего`WKWebView`**

```
func webView(_ webView: WKWebView, didCommit navigation: WKNavigation!) {
    viewModel.syncMindboxDeviceUUIDs(with: webView)

    let message = "[WebView]: \(#function): Content started arriving for: \(webView.url?.absoluteString ?? "Unknown URL")"
    Mindbox.logger.log(level: .debug, message: message)
}
```

# Пример реализации

#### ViewModel

```
import Observation
import WebKit
import Mindbox

@Observable final class ViewModel {

    /// Синхронизация deviceUUID
    func syncMindboxDeviceUUIDs(with webView: WKWebView) {
        Mindbox.shared.getDeviceUUID { uuid in
            guard !uuid.isEmpty else {
                Mindbox.logger.log(level: .error, message: "[WebView]: Device UUID is empty or invalid")
                return
            }

            let script = """
                document.cookie = "mindboxDeviceUUID=\(uuid); path=/";
                window.localStorage.setItem('mindboxDeviceUUID', '\(uuid)');
            """

            DispatchQueue.main.async {
                webView.evaluateJavaScript(script) { _, error in
                    if let error = error {
                        Mindbox.logger.log(level: .error, message: "[WebView]: Error setting cookies and localStorage: \(error)")
                    } else {
                        Mindbox.logger.log(level: .default, message: "[WebView]: Cookies and localStorage set successfully.")
                    }
                }
            }
        }
    }

    /// Используйте этот метод для очистки данных WebView
    func clearAllWebsiteData() {
        let dataStore = WKWebsiteDataStore.default()
        let dataTypes = WKWebsiteDataStore.allWebsiteDataTypes()

        dataStore.removeData(ofTypes: dataTypes, modifiedSince: Date.distantPast) {
            Mindbox.logger.log(level: .default, message: "[WebView]: All web data cleared")
        }
    }
}

extension ViewModel {

    /// Можно использовать для вывода и проверки deviceUUID
    func viewCookiesAndLocalStorage(with webView: WKWebView) {
        print("\n" + #function)

        Mindbox.shared.getDeviceUUID { uuid in
            let message = "[WebView]: Mobile SDK UUID: \(uuid)"
            print(message)
            Mindbox.logger.log(level: .default, message: message)
        }
        
        let script = """
            JSON.stringify({
                cookies: document.cookie || "No cookies found",
                localStorage: window.localStorage.getItem('mindboxDeviceUUID') || "No value found"
            })
        """

        DispatchQueue.main.async {
            webView.evaluateJavaScript(script) { result, error in
                if let error = error {
                    let message = "[WebView]: Error retrieving cookies and localStorage: \(error)"
                    print(message)
                    Mindbox.logger.log(level: .error, message: message)
                } else {
                    let message = "[WebView]: Cookies and LocalStorage: \(result ?? "nil")"
                    print("Start===============")
                    print("Cookies and LocalStorage: \(result ?? "nil")")
                    print("===============End\n")
                    Mindbox.logger.log(level: .default, message: message)
                }
            }
        }
    }
}
```

#### WebView

#### ContentView
