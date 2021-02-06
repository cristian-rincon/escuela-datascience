# Intro to Selenium

## Basic reqs

- Python 3.6^
- Selenium
- PyUnitReport

## Unittest (PyTest) basic concepts

- Test Fixture: Preparations before & after test.
- Test Cases: code unit to be tested.
- Test Suite: a collection of Test Cases.
- Test Runner: execution orchestator.
- Test Report: summary of results.

## Find elements by

- ID
- Attribute name
- Class name
- Tag name
- XPath
- CSS Selector
- Link text
- Partial link text

## Assertions

Methods that allows you to validate expected value of the test execution. Tests will continue running if the result is true, else will stop.

## Clase WebDriver

Cuenta con una serie de propiedades y métodos para interactuar directamente con la ventana del navegador y sus elementos relacionados, como son pop-ups o alerts. Por ahora nos centraremos a las más utilizadas.

### Propiedades de la clase WebDriver

Estas son las más comunes para acceder al navegador.

| Propiedad/Atributo    | Descripción                                                                     | Ejemplo               |
| --------------------- | ------------------------------------------------------------------------------- | --------------------- |
| current_url           | Obtiene la URL del sitio en la que se encuentra el navegador                    | driver.get_url        |
| current_window_handle | Obtiene la referencia que identifica a la ventana activa en ese momento driver. | current_window_handle |
| name                  | Obtiene el nombre del navegador subyacente para la instancia activa             | driver.name           |
| orientation           | Obtiene la orientación actual del dispositivo móvil                             | driver.orientation    |
| page_source           | Obtiene el código fuente de disponible del sitio web                            | driver.page_source    |
| title                 | Obtiene el valor de la etiqueta <title> del sitio web                           | driver.title          |

## Clase WebElement

Esta clase nos permite interactuar específicamente con elementos de los sitios web como textbox, text area, button, radio button, checkbox, etc.

Propiedades más comunes de la clase WebElement

| Propiedad/Atributo | Descripción                                        | Ejemplo        |
| ------------------ | -------------------------------------------------- | -------------- |
| size               | Obtiene el tamaño del elemento                     | login.size     |
| tag_name           | Obtiene el nombre de la etiqueta HTML del elemento | login.tag_name |
| text               | Obtiene el texto del elemento                      | login.text     |

### Métodos más comunes de la clase WebElement

| Método/Atributo                      | Descripción                                                                        | Ejemplo                                          |
| ------------------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------ |
| clear()                              | Limpia el contenido de un textarea                                                 | first_name.clear()                               |
| click()                              | Hace clic en el elemento                                                           | send_button.click()                              |
| get_attribute(name)                  | Obtiene el valor del atributo de un elemento submit_button.get_attribute(‘value’)  | last_name.get_attribute(max_length)              |
| is_displayed()                       | Verifica si el elemento está a la vista al usuario                                 | banner.is_displayed()                            |
| is_enabled()                         | Verifica si el elemento está habilitado                                            | radio_button.is_enabled()                        |
| is_selected()                        | Verifica si el elemento está seleccionado, para el caso de checkbox o radio button | checkbox.is_selected()                           |
| send_keys(value)                     | Simula escribir o presionar teclas en un elemento                                  | email_field.send_keys(‘team@platzi.com’)         |
| submit()                             | Envía un formulario o confirmación en un text area                                 | search_field.submit()                            |
| value_of_css_property(property_name) | Obtiene el valor de una propiedad CSS del elemento                                 | header.value_of_css_property(‘background-color’) |
