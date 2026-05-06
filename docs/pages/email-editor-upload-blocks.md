---
title: Подготовка и разметка верстки для загрузки блоков
slug: "email-editor-upload-blocks"
source_url: "https://help.mindbox.ru/docs/email-editor-upload-blocks"
vcs_path: "email-editor-upload-blocks.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Конструктор писем Mindbox
  - Загрузка блоков для конструктора
fetched_at: "2026-05-05T06:48:43Z"
content_hash: "sha256:598f49ec1cc3654f66630c258af5e652dacd570e483f8b6fd1c2a7213e9c2834"
deprecation_hint:
  - не используется
---

# Подготовка и разметка верстки для загрузки блоков

Эта инструкция описывает, как сверстать и разметить HTML‑письмо, чтобы его части стали настраиваемыми блоками в конструкторе Mindbox.

- **Блок** — самостоятельная часть письма (шапка, баннер, карточка товара, футер). В коде это обычно контейнер `<table>`.
- **Элемент** — составляющая блока (текст, картинка, кнопка, иконка). У элемента есть контентные (например, текст кнопки, картинки) и стилевые (например, цвет, ширина, отступы, выравнивание) настройки.

## Быстрый старт

Для быстрого страта используйте готовые примеры верстки для каждого из типов блоков.

[Блок](email-editor-upload-blocks.md#block-example)

Эталонная верстка блока

Эталонная разметка блока

JSON-разметка параметров

```
<table width="100%" align="center" border="0" cellpadding="0" cellspacing="0" role="none" style="border-collapse:collapse;width:100%;table-layout:fixed !important;">
  <tr>
    <td align="center" style="padding:0;margin:0;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="none" width="600"
              bgcolor="#F5F5F5"
              style="border-collapse:separate;width:600px;background-color:#F5F5F5;border:1px solid #E0E0E0;border-radius:8px;">
        <tr>
          <td align="left" style="padding:20px 20px 20px 20px;">
            Контент блока
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

```
<!-- EDITOR_BLOCK_TEMPLATE: instruction_blocksettings-->

<table width="100%" align="center" cellspacing="0" cellpadding="0" role="none"
        style="border-collapse:collapse;width:100%;table-layout:fixed !important;max-width:600px;">
  <tr>
    <td align="center" style="padding:0;margin:0;">
      <!-- контейнер без фона -->
      <table align="center" cellspacing="0" cellpadding="0" role="none" width="600"
              style="border-collapse:separate;width:600px;">
        <tr>
          <!-- весь фон и визуальные рамки на td -->
          <td align="center"
              bgcolor="${editor.background.color}"
              ${ if(editor.background.type = "image", 'background="' & editor.background.image & '"', "" ) }
              style="${editor.background.formattedBackgroundStyles};
                      border:${editor.box_border};
                      border-radius:${editor.box_radius};
                      padding:${editor.block_padding.formattedValue};">

          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

```
[
  {
    "name": "background",
    "type": "BACKGROUND",
    "defaultValue": {
      "type": "color",
      "color": "#FFFFFF"
    },
    "role": null,
    "group": "#90 Фон блока"
  },
  {
    "name": "box_border",
    "type": "BORDER",
    "defaultValue": "solid #E0E0E0 1",
    "role": null,
    "group": "#1400 Обводка"
  },
  {
    "name": "box_radius",
    "type": "BORDER_RADIUS",
    "defaultValue": "8 8 8 8",
    "role": null,
    "group": "#1500 Скругления"
  },
  {
    "name": "block_padding",
    "type": "INNER_SPACING",
    "defaultValue": "20 20 20 20",
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  }
]
```

---

[Текст](email-editor-upload-blocks.md#text-example)

Эталонная верстка текста

Эталонная разметка текста

JSON-разметка параметров текста

```
<table width="600" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    <td align="left" bgcolor="#FFFFFF" 
    style="padding:20px; border:1px solid #DDDDDD; border-radius:4px;">
      <div style="font-family:Tahoma, Arial, 
      sans-serif; font-size:16px; line-height:1.5; 
                  color:#000000; text-align:left;">
                Привет, я хорошо сверстанный текстовый элемент
      </div>
    </td>
  </tr>
</table>
```

```
<!-- EDITOR_BLOCK_TEMPLATE: instruction_text-->

<table width="600" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    @{if editor.shouldshowtext}
    <td align="${editor.text_align.align}" bgcolor="#FFFFFF" 
    style="padding: ${editor.text_padding.formattedValue}; border:${editor.border_style}; border-radius: ${editor.border_radius};">
      <div style="font-family:${editor.text_styles.formattedValue};">
                ${editor.text}
      </div>
    </td>
  </tr>@{end if}
</table>
```

```
[
  {
    "name": "shouldshowtext",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": null
  },
  {
    "name": "text_align",
    "type": "ALIGN",
    "defaultValue": "center",
    "extra": null,
    "role": null,
    "group": "#1600 Отступы и выравнивание"
  },
  {
    "name": "text_padding",
    "type": "INNER_SPACING",
    "defaultValue": "20 20 20 20",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "border_style",
    "type": "BORDER",
    "defaultValue": "solid #DDDDDD 1",
    "extra": null,
    "role": null,
    "group": "#1400 Обводка"
  },
  {
    "name": "border_radius",
    "type": "BORDER_RADIUS",
    "defaultValue": "8 8 8 8",
    "extra": null,
    "role": null,
    "group": "#1500 Скругления"
  },
  {
    "name": "text_styles",
    "type": "TEXT_STYLES",
    "defaultValue": {
      "font": "Tahoma",
      "fontSize": "20",
      "lineHeight": "1.0",
      "inscription": [
        "bold"
      ],
      "fallbackFont": "Verdana",
      "letterSpacing": "",
      "color": "#000000"
    },
    "extra": null,
    "role": null,
    "group": "#900 Текст"
  },
  {
    "name": "text",
    "type": "TEXT",
    "defaultValue": "Привет, я хорошо сверстанный текстовый элемент",
    "extra": null,
    "role": null,
    "group": "#800 Текст"
  }
]
```

Результат в конструкторе

![email-editor-upload-blocks-text-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-upload-blocks-text-example.png)

---

[Картинка](email-editor-upload-blocks.md#img-example)

Эталонная верстка картинки

Эталонная разметка картинки

JSON-разметка параметров картинки

```
<table width="600" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    <td align="center" style="padding:10px;">
      <a href="#" target="_blank">
        <img src="#" 
              alt="Пример картинки" 
              width="300" height="200" border="0"
              style="display:block; border:1px solid #CCCCCC; border-radius:6px;">
      </a>
    </td>
  </tr>
</table>
```

```
<!-- EDITOR_BLOCK_TEMPLATE: instruction_picture-->

<table width="600" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    @{if editor.shouldshow_picture}
    <td style="padding:${editor.picture_padding.formattedValue}; align:${editor.picture_align.align};">
      <a href="${editor.image_link}" target="_blank">
        <img src="${editor.image_src}" 
              alt="${editor.image_alt}"
              width="${editor.size.style.formattedWidthAttribute}" 
              border="0"
              style="display:block; border:${editor.picture_border}; border-radius:${editor.picture_border_radius}; ${editor.size.formattedValue}; width:${editor.size.style.formattedWidthAttribute} !important;">
      </a>
    </td>@{end if}
  </tr>
</table>
```

```
[
  {
    "name": "image_src",
    "type": "IMAGE",
    "defaultValue": "https://example.com",
    "extra": null,
    "role": null,
    "group": "#200 Картинка"
  },
  {
    "name": "image_alt",
    "type": "ALT",
    "defaultValue": "Пример картинки",
    "extra": null,
    "role": null,
    "group": "#500 Настройки картинки"
  },
  {
    "name": "image_link",
    "type": "URL",
    "defaultValue": "https://example.com",
    "extra": null,
    "role": null,
    "group": "#100 Ссылка перехода по клику"
  },
  {
    "name": "size",
    "type": "SIZE",
    "defaultValue": "fixed 300 200",
    "extra": {
      "allowedTypes": [
        "inherit",
        "manual"
      ]
    },
    "role": null,
    "group": "#700 Настройки картинки"
  },
  {
    "name": "shouldshow_picture",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": null
  },
  {
    "name": "picture_align",
    "type": "ALIGN",
    "defaultValue": "center",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "picture_padding",
    "type": "INNER_SPACING",
    "defaultValue": "10 10 10 10",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "picture_border",
    "type": "BORDER",
    "defaultValue": "none",
    "extra": null,
    "role": null,
    "group": "#1400 Обводка"
  },
  {
    "name": "picture_border_radius",
    "type": "BORDER_RADIUS",
    "defaultValue": "5 5 5 5",
    "extra": null,
    "role": null,
    "group": "#1500 Скругления"
  }
]
```

Результат в конструкторе

![email-editor-upload-blocks-img-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-upload-blocks-img-example.png)

---

[Кнопка](email-editor-upload-blocks.md#button-example)

Эталонная верстка кнопки

Эталонная разметка кнопки

JSON-разметка параметров кнопки

```
<table border="0" cellpadding="0" cellspacing="0" width="100%">
  <tr>
  <td align="left">
    <a href="#" style="display: inline-block;">
      <table border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td
            align="center"
            valign="middle"
            style="height: 30px;
            width: 52px; 
            background-color: #ffffff; 
            border-radius: 4px;
            border: 1px solid #000000
            font-size: 18px; color: #000000; font-family: Arial, Tahoma, sans-serif; line-height: 1.5;"
          >
            ${editor.buttonText}
          </td>
        </tr>
      </table>
    </a>
  </td>
  </tr>
</table>
```

```
<!-- EDITOR_BLOCK_TEMPLATE: instruction_button-->

@{if editor.shouldshowbutton}
              <td align="center" valign="top" 
              style="padding:${editor.buttonarea_padding.formattedValue};">
                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                  <tr>
                    <td align="center">
                      <a href="${editor.button_link}" 
                      style="display:inline-block;text-decoration:none;width:100%">
                        <table border="0" cellpadding="0" 
                        width="${editor.buttonSize.width}" 
                        style="width:${editor.buttonSize.formattedWidth}" 
                        class="${editor.buttonSize.class}">
                          <tr>
                            <td align="center" valign="middle" 
                            height="${editor.buttonSize.height}" 
                            style="height:${editor.buttonSize.formattedHeight}; 
                            background-color:${editor.button_bg.color}; 
                            border:${editor.button_border}; 
                            border-radius:${editor.button_radius}; 
                            ${editor.button_textstyles.formattedValue}" 
                            class="${editor.buttonSize.class}">
                              ${editor.button_text}
                            </td>
                          </tr>
                        </table>
                      </a>
                    </td>
                  </tr>
                </table>
              </td>
              @{end if}
```

```
[
  {
    "name": "shouldshowbutton",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": null
  },
  {
    "name": "buttonarea_padding",
    "type": "INNER_SPACING",
    "defaultValue": "10 10 10 10",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "button_link",
    "type": "URL",
    "defaultValue": "https://example.com",
    "extra": null,
    "role": null,
    "group": "#100 Ссылка перехода по клику"
  },
  {
    "name": "buttonSize",
    "type": "BUTTON_SIZE",
    "defaultValue": {
      "width": "pixels 100 80",
    "height": "50 40"
    },
    "extra": null,
    "role": null,
    "group": "#750 Настройки кнопки"
  },
  {
    "name": "button_bg",
    "type": "BACKGROUND",
    "defaultValue": {
      "type": "color",
      "color": "#FFFFFF"
    },
    "role": null,
    "group": "#90 Фон кнопки"
  },
  {
    "name": "button_border",
    "type": "BORDER",
    "defaultValue": "solid #E0E0E0 1",
    "role": null,
    "group": "#1400 Обводка"
  },
  {
    "name": "button_radius",
    "type": "BORDER_RADIUS",
    "defaultValue": "8 8 8 8",
    "role": null,
    "group": "#1500 Скругления"
  },
  {
    "name": "button_textstyles",
    "type": "SIMPLE_TEXT_STYLES",
    "defaultValue": {
      "font": "Tahoma",
      "fontSize": "14",
      "lineHeight": "1.0",
      "inscription": [
        "bold"
      ],
      "fallbackFont": "Verdana",
      "letterSpacing": "",
      "color": "#000000"
    },
    "extra": null,
    "role": null,
    "group": "#1100 Текст"
  },
  {
    "name": "button_text",
    "type": "SIMPLE_TEXT",
    "defaultValue": "Перейти",
    "extra": null,
    "role": null,
    "group": "#1000 Текст"
  }
]
```

Результат в конструкторе

![email-editor-upload-blocks-button-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-upload-blocks-button-example.png)

---

[Товарная сетка](email-editor-upload-blocks.md#product-example)

Эталонная верстка товарной коллекции

Эталонная разметка товарной коллекции

JSON-разметка параметров товарной коллекции

```
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" role="presentation" style=" max-width: 600px; border-collapse:collapse;">
  <tr>
    <!-- Карточка №1: ширина ячейки в процентах, чтобы не перестраивалась -->
    <td valign="top" width="50%" style="width:50%;padding:8px;">
      <a href="https://example.com/product1" target="_blank" style="text-decoration:none;display:block;">
        <img src="https://via.placeholder.com/600x400" alt="Название товара 1"
              width="100%" height="180"
              style="display:block;border:0;border-radius:6px;height:180px;">
        <div style="padding:10px 12px;">
          <!-- Название с фиксированной высотой -->
          <div style="font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:20px;
                      color:#000;margin:0 0 8px;height:40px;overflow:hidden;">
            Название товара 1 в две строки максимум
          </div>
          <!-- Цена с фиксированной высотой -->
          <div style="font-family:Tahoma,Arial,sans-serif;font-size:16px;line-height:22px;
                      font-weight:bold;color:#111;margin:0 0 12px;height:22px;overflow:hidden;">
            5 990 ₽
          </div>
          <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation">
            <tr>
              <td align="center" height="40"
                  style="height:40px;background:#4CAF50;border:1px solid #4CAF50;border-radius:6px;
                          font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:40px;
                          color:#FFFFFF;text-decoration:none;">
                Купить
              </td>
            </tr>
          </table>
        </div>
      </a>
    </td>

    <!-- Карточка №2 -->
    <td valign="top" width="50%" style="width:50%;padding:8px;">
      <a href="https://example.com/product2" target="_blank" style="text-decoration:none;display:block;">
        <img src="https://via.placeholder.com/600x400" alt="Название товара 2"
              width="100%" height="180"
              style="display:block;border:0;border-radius:6px;height:180px;">
        <div style="padding:10px 12px;">
          <div style="font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:20px;
                      color:#000;margin:0 0 8px;height:40px;overflow:hidden;">
            Название товара 2
          </div>
          <div style="font-family:Tahoma,Arial,sans-serif;font-size:16px;line-height:22px;
                      font-weight:bold;color:#111;margin:0 0 12px;height:22px;overflow:hidden;">
            7 490 ₽
          </div>
          <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation">
            <tr>
              <td align="center" height="40"
                  style="height:40px;background:#4CAF50;border:1px solid #4CAF50;border-radius:6px;
                          font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:40px;
                          color:#FFFFFF;text-decoration:none;">
                Купить
              </td>
            </tr>
          </table>
        </div>
      </a>
    </td>
  </tr>

  <!-- Общая кнопка под сеткой в том же блоке -->
  <tr>
    <td colspan="2" align="center" style="padding:8px 0 0 0;">
      <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation">
        <tr>
          <td align="center" height="44"
              style="height:44px;background:#1F7CFF;border:1px solid #1F7CFF;border-radius:8px;
                      font-family:Tahoma,Arial,sans-serif;font-size:15px;line-height:44px;
                      color:#FFFFFF;text-decoration:none;">
            Смотреть все товары
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

```
<!-- EDITOR_BLOCK_TEMPLATE: instruction_products-->

@{if editor.shouldshowproducts}
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
        style="width:100%;max-width:600px;background-color:${editor.bgcolor};border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;font-size:0;line-height:normal;">
  <tbody>
    <tr>
      <td align="center" valign="top" style="padding:${editor.product_padding.formattedValue};">

        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
                style="width:100%;border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;font-size:0;line-height:normal;">
          <tbody>

            @{for row in Tablerows(editor.collection, 2)}
            <tr>
              @{for cell in row.Cells} 
              @{if cell.Value != null}
              <td align="left" valign="top" width="50%" style="width:50%;">
                <!-- CARD -->
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center"
                        style="width:100%;max-width:280px;background-color:${editor.product_bgcolor};border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;">
                  <tbody>
                    <tr>
                      <td align="left" valign="top" style="padding:0;">

                        <!-- ONE-LINK -->
                        <a href="${editor.link}" target="_blank" style="display:block;text-decoration:none !important;">

                          <!-- IMAGE -->
                          @{if editor.shouldShowProductImage}
                          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
                            <tbody>
                              <tr>
                                <td align="center" valign="middle"
                                    style="padding:${editor.image_td_padding.formattedValue};height:${editor.height.formattedHeight};"
                                    class="${editor.height.class}">
                                  <img src="${editor.image_1}" alt="${editor.image_alt_1}"
                                        style="display:block;width:100%;max-width:260px;height:auto;border-radius:${editor.image_radius};border:0;outline:none;text-decoration:none !important;-ms-interpolation-mode:bicubic;">
                                </td>
                              </tr>
                            </tbody>
                          </table>
                          @{end if}

                          <!-- PRICE ROW -->
                          <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
                            <tbody>
                              <tr>
                                @{if editor.shouldShowProductLabel}
                                <td align="left" valign="middle">
                                  <div style="padding:${editor.label_padding.formattedValue};border-radius:${editor.label_radius};${editor.product_price_textstyles.formattedValue};">
                                    ${editor.label_1}
                                  </div>
                                </td>
                                @{end if}
                                @{if editor.shouldShowProductOldPrice}
                                <td align="left" valign="middle" style="padding:${editor.oldprice_padding.formattedValue};">
                                  <div style="${editor.oldprice_styles.formattedValue};">
                                    ${editor.oldprice_1}
                                  </div>
                                </td>
                                @{end if}
                              </tr>
                            </tbody>
                          </table>

                          <!-- TITLE -->
                          @{if editor.shouldShowProductTitle}
                          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
                            <tbody>
                              <tr>
                                <td align="left" style="padding:${editor.title_td_padding.formattedValue};" height="${editor.textSize.containerHeightAttribute};"
                                  class="${ editor.textSize.containerClass }"
                                  style="display: block; ${ editor.textSize.containerStyle };">
                              <div style="${editor.title_styles.formattedValue};">
                                    ${editor.title_1}
                              </div>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                          @{end if}

                          <!-- BUTTON AREA -->
                          @{if editor.shouldShowProductButton}
                          <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;">
                            <tbody>
                              <tr>
                                <td align="center" valign="top" style="padding:${editor.buttonarea_padding.formattedValue};">
                                  <table role="presentation" cellpadding="0" cellspacing="0" border="0"
                                          width="${editor.buttonSize.width}"
                                          style="width:${editor.buttonSize.formattedWidth};border-collapse:collapse;"
                                          class="${editor.buttonSize.class}">
                                    <tbody>
                                      <tr>
                                        <td align="center" valign="middle" class="${editor.buttonSize.class}"
                                            height="${editor.buttonSize.height}"
                                            style="height:${editor.buttonSize.formattedHeight};background-color:${editor.button_bg};border:${editor.button_border};border-radius:${editor.button_radius};${editor.button_textstyles.formattedValue};">
                                          ${editor.button_text}
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                          @{end if}
                        </a>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
              @{end if}              
              @{end for}
            </tr>
            @{end for}
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>
@{end if}
```

Чтобы в продуктовую сетку могли подтягиваться данные, нужно заполнить значение `role` в JSON. Подробнее в [справочнике значений](email-editor-upload-blocks.md#parametry-tovarnoj-setki).

```
[
  {
    "name": "collection",
    "type": "COLLECTION",
    "defaultValue": {
      "size": 2
    }
  },
  {
    "name": "bgcolor",
    "type": "COLOR",
    "defaultValue": "#FFFFFF",
    "extra": null,
    "role": null,
    "group": "#600 Фон блока"
  },
  {
    "name": "shouldshowproducts",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": null
  },
  {
    "name": "product_padding",
    "type": "INNER_SPACING",
    "defaultValue": "10 10 10 10",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы"
  },
  {
    "name": "product_bgcolor",
    "type": "COLOR",
    "defaultValue": "#ffffff",
    "extra": null,
    "role": null,
    "group": "#600 Внутренний фон блока"
  },
  {
    "name": "link",
    "type": "URL",
    "defaultValue": "",
    "extra": null,
    "role": "ProductUrl",
    "group": "#100 Ссылка перехода по клику"
  },
  {
    "name": "shouldShowProductImage",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": "Карточка товара: картинка"
  },
  {
    "name": "image_td_padding",
    "type": "INNER_SPACING",
    "defaultValue": "0 10 10 10",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "height",
    "type": "HEIGHTV2",
    "defaultValue": "260 150 manual",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "image_1",
    "type": "IMAGE",
    "defaultValue": "https://example.com",
    "extra": null,
    "role": "ProductImageUrl",
    "group": "#200 Картинка"
  },
  {
    "name": "image_alt_1",
    "type": "ALT",
    "defaultValue": "Товар",
    "extra": null,
    "role": null,
    "group": "#500 Настройки картинки"
  },
  {
    "name": "image_radius",
    "type": "BORDER_RADIUS",
    "defaultValue": "25 25 25 25",
    "extra": null,
    "role": null,
    "group": "#1500 Скругления"
  },
  {
    "name": "shouldShowProductLabel",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": "Карточка товара: лейбл"
  },
  {
    "name": "label_padding",
    "type": "INNER_SPACING",
    "defaultValue": "5 5 5 5",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "label_radius",
    "type": "BORDER_RADIUS",
    "defaultValue": "8 8 8 8",
    "extra": null,
    "role": null,
    "group": "#1500 Скругления"
  },
  {
    "name": "product_price_textstyles",
    "type": "SIMPLE_TEXT_STYLES",
    "defaultValue": {
      "font": "Roboto",
      "fontSize": "16",
      "lineHeight": "1.15",
      "inscription": [
        "bold"
      ],
      "fallbackFont": "Arial",
      "letterSpacing": "0.2",
      "color": "#010101"
    },
    "extra": null,
    "role": null,
    "group": "#1100 Текст"
  },
  {
    "name": "label_1",
    "type": "SIMPLE_TEXT",
    "defaultValue": "1234,56",
    "extra": null,
    "role": "ProductPrice",
    "group": "#1000 Текст"
  },
  {
    "name": "shouldShowProductOldPrice",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": "Карточка товара: старая цена"
  },
  {
    "name": "oldprice_padding",
    "type": "INNER_SPACING",
    "defaultValue": "10 10 10 10",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "oldprice_styles",
    "type": "SIMPLE_TEXT_STYLES",
    "defaultValue": {
      "font": "Roboto",
      "fontSize": "12",
      "lineHeight": "1.15",
      "inscription": [
        "crossed"
      ],
      "fallbackFont": "Arial",
      "letterSpacing": "0.2",
      "color": "#999"
    },
    "extra": null,
    "role": null,
    "group": "#1100 Текст"
  },
  {
    "name": "oldprice_1",
    "type": "SIMPLE_TEXT",
    "defaultValue": "",
    "extra": null,
    "role": "ProductOldPrice",
    "group": "#1000 Текст"
  },
  {
    "name": "shouldShowProductTitle",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": "Карточка товара: название"
  },
  {
    "name": "title_td_padding",
    "type": "INNER_SPACING",
    "defaultValue": "0 0 0 0",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "textSize",
    "type": "TEXT_SIZE",
    "defaultValue": "70 70",
    "extra": null,
    "role": null,
    "group": "#1700 Отступы и выравнивание"
  },
  {
    "name": "title_styles",
    "type": "SIMPLE_TEXT_STYLES",
    "defaultValue": {
      "font": "Roboto",
      "fontSize": "18",
      "lineHeight": "1.15",
      "inscription": [
        "bold"
      ],
      "fallbackFont": "Arial",
      "letterSpacing": "0.2",
      "color": "#000000"
    },
    "extra": null,
    "role": null,
    "group": "#1100 Текст"
  },
  {
    "name": "title_1",
    "type": "TEXT",
    "defaultValue": "1",
    "extra": null,
    "role": "ProductTitle",
    "group": "#1000 Карточка товара: название"
  },
  {
    "name": "shouldShowProductButton",
    "type": "DISPLAY_TOGGLE",
    "defaultValue": "true",
    "extra": null,
    "role": null,
    "group": "Карточка товара: кнопка"
  },
  {
    "name": "buttonarea_padding",
    "type": "INNER_SPACING",
    "defaultValue": "0 0 20 0",
    "extra": null,
    "role": null,
    "group": "#1900 Отступы и выравнивание"
  },
  {
    "name": "buttonSize",
    "type": "BUTTON_SIZE",
    "defaultValue": {
      "width": "pixels 190 80",
      "height": "40 40"
    },
    "extra": null,
    "role": null,
    "group": "#750 Настройки кнопки"
  },
  {
    "name": "button_bg",
    "type": "COLOR",
    "defaultValue": "#eb5757",
    "extra": null,
    "role": null,
    "group": "#700 Настройки кнопки"
  },
  {
    "name": "button_border",
    "type": "BORDER",
    "defaultValue": "none",
    "extra": null,
    "role": null,
    "group": "#1400 Обводка"
  },
  {
    "name": "button_radius",
    "type": "BORDER_RADIUS",
    "defaultValue": "12 12 12 12",
    "extra": null,
    "role": null,
    "group": "#1500 Скругления"
  },
  {
    "name": "button_textstyles",
    "type": "SIMPLE_TEXT_STYLES",
    "defaultValue": {
      "font": "Roboto",
      "fontSize": "16",
      "lineHeight": "1.15",
      "inscription": [],
      "fallbackFont": "Arial",
      "letterSpacing": "0.2",
      "color": "#ffffff"
    },
    "extra": null,
    "role": null,
    "group": "#1100 Текст"
  },
  {
    "name": "button_text",
    "type": "SIMPLE_TEXT",
    "defaultValue": "В корзину",
    "extra": null,
    "role": null,
    "group": "#1000 Текст"
  }
]
```

Результат в конструкторе

![email-editor-upload-blocks-product-example.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-upload-blocks-product-example.png)

## Подготовка HTML-верстки

На этом этапе необходимо сверстать письмо так, чтобы его можно было разбить на блоки и элементы.

Закладывайте в верстку все параметры, которые в дальнейшем понадобятся для редактирования письма. В дальнейшем вместо значений по умолчанию (текст, цвета, ссылки, цифры) будут подставляться данные, которые можно настроить через интерфейс конструктора.

### Блоки

Каждый блок должен иметь в коде:

- фон, заданный цветом или картинкой (`bgcolor`, `background-image`);
- обводку контейнера таблицы (`border`) и скругления углов (`border-radius`);
- Внутренние отступы (`padding`) в теге `<td>`.

**Пример верстки:**

```
<table width="600" border="0" cellspacing="0" cellpadding="0"
   align="center" bgcolor="#FFFFFF"
   style="border:1px solid #E0E0E0; border-radius:8px;">
 <tr>
  <td style="padding:20px 30px 20px 30px;">
   <!-- Контент блока -->
  </td>
 </tr>
</table>
```

### Элементы

Каждый элемент в письме должен обладать набором настроек. Рекомендуем изначально заложить максимальный набор настроек. Это позволит пользователю наиболее гибко настраивать содержимое письма в конструкторе без редактирования HTML-кода.

Текст

Картинка

Кнопка

Товарная сетка

Содержимое текста должно быть указано внутри тега `<div>`. Для форматирования текста (цвет, жирность, стили) можно использовать строковый контейнер `<span>`.

Вывод текста в теге `<p>` не поддерживается.

Каждый текстовый элемент должен иметь:

- Inline-стили текста (цвет, шрифт, размер, жирность);
- Обводка (`border`) и закругление углов (`border-radius`);
- Отступы (`padding`) внутри тега `<td>`;
- Выравнивание (`align`) внутри тега `<td>`.

**Пример верстки:**

```
  <table width="600" border="0" cellspacing="0" cellpadding="0" align="center">
   <tr>
    <td align="left" bgcolor="#FFFFFF"
      style="padding:20px; border:1px solid #DDDDDD; border-radius:4px;">
     <div style="font-family:Tahoma, Arial,
       sans-serif; font-size:16px; line-height:1.5;
       color:#000000; text-align:left;">
       Привет, я хорошо сверстанный текстовый элемент
     </div>
    </td>
   </tr>
  </table>
```

Рекомендуемые настройки:

- Путь к картинке (атрибут `src`);
- Альтернативный текст картинки (атрибут `alt`);
- Ссылка по клику на картинку (`<a href>`);
- Размеры: ширина (`width`) и высота (`height`);
- Обводка (`border`) и закругление углов (`border-radius`);
- Отступы (`padding`) внутри тега `<td>`;
- Выравнивание (`align`) внутри тега `<td>`.

**Пример верстки:**

```
<table width="600" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
  <td align="center" style="padding:10px;">
    <a href="#" target="_blank">
    <img src="#"
    alt="Пример картинки"
    width="300" height="200" border="0"   
    style="display:block; border:1px solid #CCCCCC; border-radius:6px;">
    </a>
  </td>
  </tr> 
</table>
```

Рекомендуемые настройки:

- Ссылка (`<a href>`) на всю площадь кнопки;
- Текст кнопки. Указывайте текст внутри тега `<td>`. **Текст в теге `<p>` не поддерживается**;
- Фоновый цвет кнопки (`background-color`);
- Размеры кнопки: ширина (`width`) и высота (`height`);
- Стили текста (семейство, размер, начертание, цвет, `text-decoration:none`);
- Обводка (`border`) и закругление углов (`border-radius`);
- Отступы (`padding`) внутри тега `<td>`;
- Выравнивание (`align`) внутри тега `<td>`;
- Используйте таблицу (`<table>`) внутри ссылки или «bulletproof» с VML для Outlook для корректного отображения кнопки в email-письме.

**Пример верстки:**

```
<table border="0" cellpadding="0" cellspacing="0" width="100%">
 <tr>
  <td align="left">
    <a href="#" style="display: inline-block;">
      <table border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td
            align="center"
            valign="middle"
            style="height: 30px;
            width: 52px; 
            background-color: #ffffff; 
            border-radius: 4px;
            border: 1px solid #000000
            font-size: 18px; color: #000000; font-family: Arial, Tahoma, sans-serif; line-height: 1.5;"
          >
            Перейти на сайт
          </td>
        </tr>
      </table>
    </a>
   </td>
  </tr>
 </table>
```

Рекомендуемые настройки:

- **Ссылка** (`<a href>`) на всю площадь карточки продукта (не только картинка и кнопка, но и название, описание, цена и др.);
- **Высота** (`height`) для всех текстовых элементов карточки продуктов (название, описание и др.). Это необходимо, чтобы карточки в одной строке были выровнены, даже если их текст разной длины;
- Укажите фиксированную высоту картинки (`height`), чтобы картинки одного размера масштабировались в зависимости от высоты;
- Используйте только строковые (inline) параметры (ссылки, тексты, стили);
- Указывайте элементы, которые относятся к товарной сетке, в составе одного блока. Например, заголовок блока («Новинки недели») или кнопка под товарами для перехода на сайт;

**Виды товарных сеток:**

- **Адаптивная** — адаптирует вывод продуктов под мобильную версию. Все продукты выводятся в одну колонку.

  [**Пример адаптивной верстки**](email-editor-upload-blocks.md#non-adaptive-html)

  ```
      <!-- Блок сетки: заголовок и общая кнопка внутри того же контейнера -->
      <div style="max-width:600px;margin:0 auto;">
      
        <!-- Заголовок -->
        <div style="font-family:Tahoma,Arial,sans-serif;font-size:20px;line-height:1.3;
                    font-weight:bold;margin:0 0 12px;">Новинки недели</div>
      
        <!-- Карточка №1 (адаптивная ширина) -->
        <div style="display:inline-block;vertical-align:top;width:48%;margin:0 1% 16px;
                    background:#FFFFFF;border:1px solid #E6E6E6;border-radius:6px;">
          <a href="https://example.com/product1" target="_blank" style="text-decoration:none;display:block;">
            <!-- Картинка фиксированной высоты, ширина по контейнеру -->
            <img src="https://via.placeholder.com/600x400" alt="Название товара 1"
                  width="100%" height="180"
                  style="display:block;border:0;border-radius:6px 6px 0 0;height:180px;">
      
            <div style="padding:10px 12px;">
              <!-- Название: фиксированная высота (2 строки по 20px) -->
              <div style="font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:20px;
                          color:#000;margin:0 0 8px;height:40px;overflow:hidden;">
                Название товара 1 в две строки максимум
              </div>
      
              <!-- Цена: фиксированная высота одной строки -->
              <div style="font-family:Tahoma,Arial,sans-serif;font-size:16px;line-height:22px;
                          font-weight:bold;color:#111;margin:0 0 12px;height:22px;overflow:hidden;">
                5 990 ₽
              </div>
      
              <!-- Кнопка внутри карточки -->
              <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation">
                <tr>
                  <td align="center" height="40"
                      style="height:40px;background:#4CAF50;border:1px solid #4CAF50;border-radius:6px;
                              font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:40px;
                              color:#FFFFFF;text-decoration:none;">
                    Купить
                  </td>
                </tr>
              </table>
            </div>
          </a>
        </div>
      
        <!-- Карточка №2 (идентичная по структуре) -->
        <div style="display:inline-block;vertical-align:top;width:48%;margin:0 1% 16px;
                    background:#FFFFFF;border:1px solid #E6E6E6;border-radius:6px;">
          <a href="https://example.com/product2" target="_blank" style="text-decoration:none;display:block;">
            <img src="https://via.placeholder.com/600x400" alt="Название товара 2"
                  width="100%" height="180"
                  style="display:block;border:0;border-radius:6px 6px 0 0;height:180px;">
      
            <div style="padding:10px 12px;">
              <div style="font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:20px;
                          color:#000;margin:0 0 8px;height:40px;overflow:hidden;">
                Название товара 2
              </div>
              <div style="font-family:Tahoma,Arial,sans-serif;font-size:16px;line-height:22px;
                          font-weight:bold;color:#111;margin:0 0 12px;height:22px;overflow:hidden;">
                7 490 ₽
              </div>
              <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation">
                <tr>
                  <td align="center" height="40"
                      style="height:40px;background:#4CAF50;border:1px solid #4CAF50;border-radius:6px;
                              font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:40px;
                              color:#FFFFFF;text-decoration:none;">
                    Купить
                  </td>
                </tr>
              </table>
            </div>
          </a>
        </div>
      
        <!-- Общая кнопка сетки (тоже внутри блока) -->
        <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation" style="margin:8px 0 0;">
          <tr>
            <td align="center" height="44"
                style="height:44px;background:#1F7CFF;border:1px solid #1F7CFF;border-radius:8px;
                        font-family:Tahoma,Arial,sans-serif;font-size:15px;line-height:44px;
                        color:#FFFFFF;text-decoration:none;">
              Смотреть все товары
            </td>
          </tr>
        </table>
      </div>
  ```
- **Неадаптивная** — карточки продуктов выводятся для десктопной и мобильной версий одинаково.

  [**Пример неадаптивной верстки**](email-editor-upload-blocks.md#non-adaptive-html)

  ```
  <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" role="presentation" style=" max-width: 600px; border-collapse:collapse;">
    <!-- Заголовок внутри блока -->
    <tr>
      <td colspan="2" style="padding:0 0 12px 0;font-family:Tahoma,Arial,sans-serif;
                              font-size:20px;line-height:1.3;font-weight:bold;">
        Хиты продаж
      </td>
    </tr>

    <tr>
      <!-- Карточка №1: ширина ячейки в процентах, чтобы не перестраивалась -->
      <td valign="top" width="50%" style="width:50%;padding:8px;">
        <a href="https://example.com/product1" target="_blank" style="text-decoration:none;display:block;">
          <img src="https://via.placeholder.com/600x400" alt="Название товара 1"
                width="100%" height="180"
                style="display:block;border:0;border-radius:6px;height:180px;">
          <div style="padding:10px 12px;">
            <!-- Название с фиксированной высотой -->
            <div style="font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:20px;
                        color:#000;margin:0 0 8px;height:40px;overflow:hidden;">
              Название товара 1 в две строки максимум
            </div>
            <!-- Цена с фиксированной высотой -->
            <div style="font-family:Tahoma,Arial,sans-serif;font-size:16px;line-height:22px;
                        font-weight:bold;color:#111;margin:0 0 12px;height:22px;overflow:hidden;">
              5 990 ₽
            </div>
            <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation">
              <tr>
                <td align="center" height="40"
                    style="height:40px;background:#4CAF50;border:1px solid #4CAF50;border-radius:6px;
                            font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:40px;
                            color:#FFFFFF;text-decoration:none;">
                  Купить
                </td>
              </tr>
            </table>
          </div>
        </a>
      </td>

      <!-- Карточка №2 -->
      <td valign="top" width="50%" style="width:50%;padding:8px;">
        <a href="https://example.com/product2" target="_blank" style="text-decoration:none;display:block;">
          <img src="https://via.placeholder.com/600x400" alt="Название товара 2"
                width="100%" height="180"
                style="display:block;border:0;border-radius:6px;height:180px;">
          <div style="padding:10px 12px;">
            <div style="font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:20px;
                        color:#000;margin:0 0 8px;height:40px;overflow:hidden;">
              Название товара 2
            </div>
            <div style="font-family:Tahoma,Arial,sans-serif;font-size:16px;line-height:22px;
                        font-weight:bold;color:#111;margin:0 0 12px;height:22px;overflow:hidden;">
              7 490 ₽
            </div>
            <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation">
              <tr>
                <td align="center" height="40"
                    style="height:40px;background:#4CAF50;border:1px solid #4CAF50;border-radius:6px;
                            font-family:Tahoma,Arial,sans-serif;font-size:14px;line-height:40px;
                            color:#FFFFFF;text-decoration:none;">
                  Купить
                </td>
              </tr>
            </table>
          </div>
        </a>
      </td>
    </tr>

    <!-- Общая кнопка под сеткой в том же блоке -->
    <tr>
      <td colspan="2" align="center" style="padding:8px 0 0 0;">
        <table border="0" cellspacing="0" cellpadding="0" width="100%" role="presentation">
          <tr>
            <td align="center" height="44"
                style="height:44px;background:#1F7CFF;border:1px solid #1F7CFF;border-radius:8px;
                        font-family:Tahoma,Arial,sans-serif;font-size:15px;line-height:44px;
                        color:#FFFFFF;text-decoration:none;">
              Смотреть все товары
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
  ```

---

## Разметка верстки на блоки

Добавьте **HTML-комментарий** в начало каждого блока:

```
<!-- EDITOR_BLOCK_TEMPLATE: system_name -->
```

`system_name` — уникальное название блока:

- Имя должно быть **уникальным** для каждого блока.
- Можно использовать **латинские буквы, цифры и знак подчеркивания (_)**;
- Если вы загружаете блок с тем же системным именем, что уже был на проекте, то он **обновляется**: новая версия полностью перезаписывает старую.

Конструктор учитывает код только **от комментария до комментария**. Все, что находится вне их, загружено не будет.

**Пример:**

```
<!-- EDITOR_BLOCK_TEMPLATE: mindbox_1 -->
<table cellspacing="0" cellpadding="0" border="0" width="100%">
 <tr>
  <td style="padding: 10px 20px 15px 5px;">
   Текст с разными отступами
  </td>
 </tr>
</table>
```

---

## Разметка элементов

Чтобы наполнение блока можно было менять и настраивать, блок необходимо разметить по элементам.

Для этого используются:

1. Параметры разметки (`${editor.*}`, `${editor.*.formattedValue}` и др.)
2. [Настройки JSON](email-editor-upload-blocks.md#svojstva-nastroek-json), которые сопоставляют параметры с нужными настройками конструктора и задают их свойства.

### Параметры разметки

Параметры вставляются на место значений в тегах или атрибутах верстки (текст, href, style, width/height и т.д.). Общий вид параметра — `${editor.<уникальное название параметра>}`.

**Требования к наименованию параметров:**

- Название должно содержать только **цифры, латиницу и подчеркивание**(_);
- Название регистро**не**зависимое: `${editor.text}` = `${editor.TEXT}`;
- Название должно быть **уникальным в рамках блока**. Если в блоке задается две переменные с одинаковым названием, то для обоих мест будет единая настройка в интерфейсе конструктора.

**Как это работает:**

1. Определите, какие элементы и их настройки необходимо добавить в блок.
2. Замените значение в теге или атрибуте на соответствующий параметр разметки из [справочника](email-editor-upload-blocks.md#spravochnik-nastroek-i-elementov). В некоторых настройках необходимо скорректировать или добавить несколько значений.

[Готовые примеры разметки элементов.](email-editor-upload-blocks.md#bystryj-start)

### Справочник настроек и элементов

Мобильное отображение

📱 Для настроек с таким знаком доступна настройка мобильного отображения. Для этого добавьте атрибут `class` с параметром `${editor.*.class}`.

[Общие настройки](email-editor-upload-blocks.md#general)

|  |  |  |  |
| --- | --- | --- | --- |
| Настройка | Место в верстке | Параметр разметки | JSON |
| Настройка скрытия и отображения элемента | Вокруг элемента | Конструкция:  ``` @{if editor.*} <!-- Элемент --> @{end if} ``` | [DISPLAY_TOGGLE](email-editor-upload-blocks.md#DISPLAY-TOGGLE) |
| Ссылка перехода (по клику на кнопку, картинку и т.д.) | В атрибуте ссылки `href` | `${editor.*}` | [URL](email-editor-upload-blocks.md#URL) |
| 📱Отступы (padding) | Атрибут `style` | `${editor.*.formattedValue}` | [INNER_SPACING](email-editor-upload-blocks.md#INNER-SPACING) |
| 📱Выравнивание  `align` и `style` должны иметь одинаковое название параметра. | Атрибут `align` | `${editor.*.align}` | [ALIGN](email-editor-upload-blocks.md#ALIGN) |
| Атрибут `style` | `${editor.*.formattedValue}` |
| Фон блока | Свойство `bgcolor` или `background-color` | `${editor.*.color}` | [BACKGROUND](email-editor-upload-blocks.md#BACKGROUND) |
| Атрибут `style` | `${editor.*.formattedBackgroundStyles}` |
| После `style` в том же теге | Добавьте строку  ``` ${if(editor.*.type = "image",  'background="' & editor.*.image & '"',  "" ) } ``` |
| Обводка блока | Свойство `border` | `${ editor.*}` | [BORDER](email-editor-upload-blocks.md#BORDER) |
| Радиус скругления границ | Тег `<td>`, атрибут `style` | `${editor.*}` | [BORDER_RADIUS](email-editor-upload-blocks.md#BORDER-RADIUS) |
| Заливка цветом | Свойство `background-color` | `${editor.*}` | [COLOR](email-editor-upload-blocks.md#COLOR) |

---

[Текст](email-editor-upload-blocks.md#text)

В конструкторе предусмотрено два типа текста:

- **Длинный текст** — используется для текстов из нескольких абзацев. Такой текст можно использовать для контентных блоков.
- **Короткий текст** — используется для элементов с текстом на одну или несколько строк. Например, кнопки или пункты меню.

|  |  |  |  |
| --- | --- | --- | --- |
| Настройка | Место в верстке | Параметр разметки | JSON |
| 📱Редактирование длинного текста | Вместо текста | `${editor.*}`. | [TEXT](email-editor-upload-blocks.md#TEXT) |
| 📱Настройка стилей длинного текста | Атрибут `style` | `${editor.*.formattedValue}` | [TEXT_STYLES](email-editor-upload-blocks.md#TEXT-STYLES) |
| 📱Редактирование короткого текста | Вместо текста | `${editor.*}`. | [SIMPLE_TEXT](email-editor-upload-blocks.md#SIMPLE-TEXT) |
| 📱Настройка стилей короткого текста | Атрибут `style` | `${editor.*.formattedValue}` | [SIMPLE_TEXT_STYLES](email-editor-upload-blocks.md#SIMPLE-TEXT-STYLES) |
| 📱Высота контейнера текста  Переменная должна быть **одинаковой в обеих конструкциях**. | Атрибут `height` | `${editor.*.containerHeightAttribute}` | [TEXT_SIZE](email-editor-upload-blocks.md#TEXT-SIZE) |
| Атрибут `style` | `${editor.*.containerStyle}` |  |

---

[Картинка](email-editor-upload-blocks.md#img)

- **Картинка** — позволяет загрузить картинку или выбрать из галереи загруженных изображений, а также настроить **персональный вывод** изображения из данных клиента или заказа.
- **Иконка** — позволяет загрузить изображение либо выбрать его из набора стандартных иконок Mindbox. Подходит для вывода контактов, адресов или оформления письма.

Доступные настройки:

|  |  |  |  |
| --- | --- | --- | --- |
| Настройка | Место в верстке | Параметр разметки | JSON |
| Ссылка на картинку | Тег `<img>`, атрибут `src` | `${editor.*}` | [IMAGE](email-editor-upload-blocks.md#IMAGE) |
| Ссылка на иконку | Тег `<img>`, атрибут `src` | `${editor.*}` | [ICON](email-editor-upload-blocks.md#ICON) |
| Alt-текст | Атрибут `alt` | `${editor.*}` | [ALT](email-editor-upload-blocks.md#ALT) |
| 📱 Ширина картинки  Переменная должна быть **одинаковой** в `width` и `style`. | Тег `<img>`, атрибут `width` | `${editor.*.style.formattedWidthAttribute}` | [SIZE](email-editor-upload-blocks.md#SIZE) |
| Тег `<img>`, атрибут `style` | ``` display: block;  ${editor.*.formattedValue};  width:${editor.*.style.formattedWidthAttribute}; ``` |
| Высота картинки  Переменная должна быть **одинаковой в обеих конструкциях**. | Тег `<img>`, атрибут `height` | `${editor.*.formattedHeight}` | [HEIGHTV2](email-editor-upload-blocks.md#HEIGHTV2) |
| Тег `<img>`, атрибут `style` | `height: ${editor.*.formattedHeight};` |

---

[Размер кнопки](email-editor-upload-blocks.md#button)

**JSON:** [BUTTON_SIZE](email-editor-upload-blocks.md#BUTTON-SIZE)

Чтобы добавить возможность менять размер кнопки в конструкторе, пропишите:

| Место в верстке | Параметр разметки |
| --- | --- |
| Атрибут `width` | `${editor.*.width}` |
| Атрибут `height` | `${editor.*.height}` |
| Атрибут `style` | `width: ${editor.*.formattedWidth}; height: ${editor.*.formattedHeight}` |
| Атрибут `class` | `${editor.*.class}` |

Переменная `*` должна быть **одинаковой во всех конструкциях**.

---

[Товарная сетка](email-editor-upload-blocks.md#product)

JSON: [COLLECTION](email-editor-upload-blocks.md#COLLECTION)

Для вывода товарной сетки:

1. Используйте разметку одной карточки продуктов. Для вывода данных продукта используйте [общие настройки](email-editor-upload-blocks.md#general) и настройки [картинок](email-editor-upload-blocks.md#img), [текста](email-editor-upload-blocks.md#text) и [кнопок](email-editor-upload-blocks.md#button).
2. Выберите конструкцию блока: адаптивная (через блок `<div>`) или неадаптивная (через `<table>`):

   - **Адаптивная конструкция** — карточки продуктов перестраиваются друг под друга в зависимости от доступной ширины устройства. Товарная сетка должна быть сверстана через `<div>`.

   ```
   <div>
     @{ for item in editor.collection }
       <!-- Карточка продукта -->
     @{ end for }
   </div>
   ```

   - **Неадаптивная конструкция** — товарная сетка отображается одинаково на десктопе и на мобильных устройствах. Товарная сетка должна быть сверстана через `<table>`.

   ```
   <table>
       <tbody>
           @{for row in Tablerows(editor.*,
           <количество колонок>)}
               <tr>
                   @{for cell in row.Cells} 
                     @{if cell.value != null}
                     <td>
                         <!-- Карточка продукта -->
                     </td>
                     @{end if} 
                   @{end for}
               </tr>
               @{end for}
       </tbody>
   </table>
   ```

## Загрузка блоков

1. Перейдите в раздел **Настройки** → **Рассылки** → **Загрузка блоков для конструктора** и загрузите подготовленный файл:

![email-editor-upload-blocks-upload.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-upload-blocks-upload.png)

Если в верстке или разметке нет ошибок, блоки появятся в списке на странице. На этом этапе блоки с переменными ещё не доступны для использования в конструкторе.

[Частые ошибки при загрузке и настройке параметров](email-editor-upload-blocks.md#chastye-oshibki)

2. Перейдите по кнопке «Изменить» для настройки свойств переменных:

![email-editor-upload-blocks-upload-not-ready.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-upload-blocks-upload-not-ready.png)

## Свойства настроек JSON

После загрузки размеченного блока необходимо задать свойства настроек через код JSON. Это необходимо, чтобы конструктор понял, какие настройки показывать в интерфейсе, какого они типа, какие значения будут подставляться по умолчанию и как сгруппировать их в шторке настроек.

![email-editor-upload-blocks-json-settings.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-upload-blocks-json-settings.png)

**Поля JSON:**

| Поле в JSON | Пояснение |
| --- | --- |
| `name` | Имя переменной. Заполняется автоматически по параметрам разметки `${editor.*}` при загрузке блока. |
| `type` | Тип настройки в интерфейсе. Полный список типов находится [здесь](email-editor-upload-blocks.md#spravochnik-svojstv-json-i). |
| `defaultValue` | Значение настройки по умолчанию, которое будет отображаться в интерфейсе конструктора. |
| `role` | Параметр динамической товарной сетки для автоматического подстановки персонализации. Подробнее [здесь](email-editor-upload-blocks.md#parametry-tovarnoj-setki). |
| `group` | Группа настроек с приоритетом сортировки. Полную таблицу приоритетов можно посмотреть [здесь](email-editor-upload-blocks.md#prioritety-nastroek-dopolnitelno). |

### Справочник свойств JSON `type` и `defaultValue`

|  |  |  |
| --- | --- | --- |
| Настройка | type | defaultValue |
| Настройка скрытия и отображения элемента | [DISPLAY_TOGGLE](email-editor-upload-blocks.md#DISPLAY-TOGGLE-param) | “true” |
| Ссылка перехода (по клику на кнопку, картинку и т.д.) | [URL](email-editor-upload-blocks.md#URL-param) | Любая ссылка в формате "https://example.ru" |
| Отступы (padding) | [INNER_SPACING](email-editor-upload-blocks.md#INNER-SPACING-param) | Значения для каждого из отступов через пробел в формате: `25 25 25 25` |
| Выравнивание | [ALIGN](email-editor-upload-blocks.md#ALIGN-param) | Доступные значения:   - “left” - “right” - “center” |
| Фон блока | [BACKGROUND](email-editor-upload-blocks.md#BACKGROUND-param) | Можно задать тремя способами: прозрачным фоном, сплошным цветом или картинкой.  **Прозрачный фон:**  `"defaultValue": {`  `"type": "transparent"}`  **Сплошной цвет:**  `"defaultValue": {`  `"type": "color",`  `"color": "<цвет>"}`  **Фон картинкой:**  `"defaultValue": {`  `"type": "image",`  `"mode": "contain / cover / repeat / stretch",`  `"color": "<цвет>",`  `"url": "<ссылка>"},` |
| Обводка блока | [BORDER](email-editor-upload-blocks.md#BORDER-param) | **Без обводки**: `"none"`.  **С обводкой**:   - тип обводки (`solid / dashed / dotted`), - цвет (`<любой цвет>`) - толщина (`<число>`) — через пробел.   Например, `"defaultValue": "solid black 2"` |
| Радиус скругления границ | [BORDER_RADIUS](email-editor-upload-blocks.md#BORDER-RADIUS-param) | Значения для каждого из углов через пробел в формате: `25 25 25 25` |
| Заливка цветом | [COLOR](email-editor-upload-blocks.md#COLOR-param) | Любой цвет в формате `#000000` |
| Редактирование длинного текста | [TEXT](email-editor-upload-blocks.md#TEXT-param) | Любой длинный текст на несколько абзацев |
| Настройка стилей длинного текста | [TEXT_STYLES](email-editor-upload-blocks.md#TEXT-STYLES-param) | Доступные значения:   - `font`: "Roboto" / "Open Sans" / "Montserrat" / "Inter" / "Arial" / "Geneva" / "Helvetica" / "Times New Roman" /"Verdana" / "Courier / Courier New" / "Tahoma" / "Georgia" / "Palatino" / "Trebuchet MS" - `fontSize`: <число> - `lineHeight`: "1.0" / "1.15" / "1.5" / "2.0" - `inscription`: "bold" / "italic" / "underlined" / "crossed". Если необходимо указать обычное начертание текста (regular) — оставьте квадратные скобки пустыми. - `fallbackFont`: "Arial" / "Geneva" / "Helvetica" / "Times New Roman" / "Verdana" / "Courier / Courier New" /"Tahoma" / "Georgia" / "Palatino" / "Trebuchet MS" - `letterSpacing`: <число>   Если в мастер-шаблоне используется кастомный шрифт, его можно зафиксировать на уровне верстки, но в таком случае менять стили в конструкторе не получится. |
| Редактирование короткого текста | [SIMPLE_TEXT](email-editor-upload-blocks.md#SIMPLE-TEXT-param) | Любой короткий текст на одну или несколько строк |
| Настройка стилей короткого текста | [SIMPLE_TEXT_STYLES](email-editor-upload-blocks.md#SIMPLE-TEXT-STYLES-param) | Доступные значения:   - `font`: "Roboto" / "Open Sans" / "Montserrat" / "Inter" / "Arial" / "Geneva" / "Helvetica" / "Times New Roman" /"Verdana" / "Courier / Courier New" / "Tahoma" / "Georgia" / "Palatino" / "Trebuchet MS" - `fontSize`: <число> - `lineHeight`: "1.0" / "1.15" / "1.5" / "2.0" - `inscription`: "bold" / "italic" / "underlined" / "crossed". Если необходимо указать обычное начертание текста (regular) — оставьте квадратные скобки пустыми. - `fallbackFont`: "Arial" / "Geneva" / "Helvetica" / "Times New Roman" / "Verdana" / "Courier / Courier New" /"Tahoma" / "Georgia" / "Palatino" / "Trebuchet MS" - `letterSpacing`: <число> - `color`: <цвет в HEX>   Если в мастер-шаблоне используется кастомный шрифт, его можно зафиксировать на уровне верстки, но в таком случае менять стили не в конструкторе не получится. |
| Высота контейнера текста | [TEXT_SIZE](email-editor-upload-blocks.md#TEXT-SIZE-param) | Значения для ширины и высоты через пробел в формате: `30 30` |
| Ссылка на картинку | [IMAGE](email-editor-upload-blocks.md#IMAGE-param) | Любая ссылка на картинку в формате "images/img.png” |
| Ссылка на иконку | [ICON](email-editor-upload-blocks.md#ICON-param) | Любая ссылка на картинку в формате "images/img.png” |
| Alt-текст | [ALT](email-editor-upload-blocks.md#ALT-param) | Любой текст |
| Ширина картинки | [SIZE](email-editor-upload-blocks.md#SIZE-param) | Доступные значения:   - `"manual 55 *"`, где `*` - любое число до 100. - объект `"extra"` со значениями:   - `"defaultMaxWidth"` — значение ширины письма;   - `"allowedTypes"`, где записываются все варианты ширины для картинки:     - `"inherit"` — «По ширине блока»,     - `"manual"` — «Настраиваемая вручную» |
| Высота картинки | [HEIGHTV2](email-editor-upload-blocks.md#HEIGHTV2-param) | Указываются 2 значения через пробел в формате `50 50 manual` |
| Размер кнопки | [BUTTON_SIZE](email-editor-upload-blocks.md#button) | Указывается тип, два значения для ширины и два дефолтных значения высоты через пробел. Первое значение для десктопной версии, второе — для мобильной.  ``` {   "width": "pixels 100 80",   "height": "50 40" } ```  Список возможных типов ширины:   - `pixels` — значение ширины в пикселях (max 600) - `percent` — значение ширины в процентах (max 100 min 10) |
| Товарная сетка | [COLLECTION](email-editor-upload-blocks.md#product) | На выбор может быть одно из значений, которое будет стоять по умолчанию при использовании блока из галереи:   - "RECIPIENT_RECOMMENDATIONS" - "FROM_SEGMENT" - "FROM_PRODUCT_LIST" - "ORDER" - "VIEWED_PRODUCTS_IN_SESSION" - "PRODUCT_LIST_ITEM" - "PRODUCT_VIEW" - "FROM_CUSTOMER_COMPUTED_FIELD"   Количество выводимых товаров задается отдельно:`"size": 2` |

### Параметры товарной сетки `role`

Параметры `role` автоматически определяют, какую [персонализацию](https://help.mindbox.ru/docs/new-builder-personalize) необходимо подставить в элементы блока.

| Элемент | **role** |
| --- | --- |
| Название продукта | ProductTitle |
| Актуальная цена продукта | ProductPrice |
| Старая цена продукта | ProductOldPrice |
| Ссылка на продукт | ProductUrl |
| Картинка продукта | ProductImageUrl |
| Описание продукта | ProductDescription |
| Дополнительные данные о продукте | ProductBadge |

Для параметров цены (`ProductOldPrice` и `ProductPrice`) необходимо указать `"type": "TEXT"`.

### Приоритеты настроек `group` (дополнительно)

Параметр `group` определяет распределение настроек по группам в интерфейсе и их порядок.

**Общая таблица приоритетов элементов:**

|  |  |
| --- | --- |
| Тип | Число |
| BACKGROUND | 90 |
| URL | 100 |
| IMAGE | 200 |
| ICON | 400 |
| ALT | 500 |
| COLOR | 600 |
| SIZE | 700 |
| HEIGHTV2 | 700 |
| BUTTON_SIZE | 750 |
| TEXT | 800 |
| TEXT_STYLES | 900 |
| SIMPLE_TEXT | 1000 |
| SIMPLE_TEXT_STYLES | 1100 |
| BORDER | 1400 |
| BORDER_RADIUS | 1500 |
| ALIGN | 1600 |
| TEXT_SIZE | 1700 |
| INNER_SPACING | 1900 |

![email-editor-upload-blocks-group.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/email-editor-upload-blocks-group.png)

*Пример группировки «Отступы и выравнивание»*

## Частые ошибки

|  |  |  |
| --- | --- | --- |
| Текст ошибки | Причина | Решение |
| Параметр "editor.*" является составным типом и не может использоваться напрямую | Использован простой параметр (`editor.example`)вместо составного (`editor.example.formattedValue`) | Обратитесь к [справочнику параметров](email-editor-upload-blocks.md#spravochnik-nastroek-i-elementov) |
| Тип является составным и не может быть использован как примитивное значение. Используйте доступ к полям (например, editor.propName.fieldName) |
| Значение поля type не соответствует ожидаемому: SIZE_IN_PERCENTS / COLLECTION | Параметры ширины картинки (SIZE) указаны некорректно или указаны не все обязательные параметры | Проверьте все параметры SIZE согласно [справочнику](email-editor-upload-blocks.md#SIZE-param) |
| Параметр "editor.*.style" имеет невалидный формат. Параметры могут содержать только 1 точку | Наименование параметра используется дважды в рамках одного блока (должно быть уникальным) | Проверьте уникальность имен параметров в блоке |
| Параметры указаны неверно | Убедитесь в корректности синтаксиса параметров по [справочнику параметров](email-editor-upload-blocks.md#spravochnik-nastroek-i-elementov) |
