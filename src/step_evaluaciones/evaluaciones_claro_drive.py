from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from src.step_evaluaciones import constantes_evaluaciones_claro_drive
from src.utils.utils_evaluaciones import UtilsEvaluaciones
from src.utils.utils_html import ValidacionesHtml
from src.utils.utils_temporizador import Temporizador
from src.webdriver_actions.html_actions import HtmlActions


class EvaluacionesClaroDriveSteps:

    @staticmethod
    def ingreso_pagina_principal_claro_drive(webdriver: WebDriver, json_eval):
        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        try:
            webdriver.get('https://www.clarodrive.com/')

            # localiza boton de inicio en la pagina principal
            HtmlActions.webdriver_wait_presence_of_element_located(webdriver, 15, id='login')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 0, 0, True, constantes_evaluaciones_claro_drive.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_EXITOSO)

        except ElementNotInteractableException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO. \
                format(e.msg)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 0, 0, False, msg_output)

        except NoSuchElementException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO.\
                format(e.msg)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 0, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO. \
                format(e.msg)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 0, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 0, tiempo_step_inicio, fecha_inicio)

        return json_eval

    @staticmethod
    def inicio_sesion_claro_drive(webdriver_test_ux: WebDriver, json_eval, argumentos_json):

        tiempo_step_inicio = None
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        try:
            btn_inicio_sesion = HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, 6, id='login')
            HtmlActions.click_html_element(btn_inicio_sesion, id='login')

            input_email = HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, 6, class_name='InputEmail')
            input_email.send_keys(argumentos_json['user'])

            input_password = HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, 6, class_name='InputPassword')
            input_password.send_keys(argumentos_json['password'])

            btn_ingreso_cuenta = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, 6, xpath='//button[text()="INICIAR SESI\u00D3N"]')
            HtmlActions.click_html_element(btn_ingreso_cuenta, xpath='//button[text()="INICIAR SESI\u00D3N"]')

            # inicia el tiempo de inicio
            tiempo_step_inicio = Temporizador.obtener_tiempo_timer()

            HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, 120, class_name='button-create-resource')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 1, 0, True, constantes_evaluaciones_claro_drive.MSG_OUTPUT_INICIO_SESION_EXITOSO)

        except ElementNotInteractableException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_INICIO_SESION_SIN_EXITO. \
                format(e.msg)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 1, 0, False, msg_output)

        except NoSuchElementException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_INICIO_SESION_SIN_EXITO. \
                format(e.msg)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 1, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_INICIO_SESION_SIN_EXITO. \
                format(e.msg)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 1, 0, False, msg_output)

        except StaleElementReferenceException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_INICIO_SESION_SIN_EXITO. \
                format(e.msg)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 1, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 1, tiempo_step_inicio, fecha_inicio)

        return json_eval

    @staticmethod
    def carga_archivo_claro_drive(webdriver_test_ux: WebDriver, path_archivo_carga: str, json_eval):

        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        # verifica que se haya iniciado sesion correctamente
        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_sesion(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 2,
                'No fue posible realizar la carga del archivo. No se ingreso a la sesion de Claro Drive correctamente')

            return json_eval

        try:
            boton_crear = HtmlActions.webdriver_wait_element_to_be_clickable(webdriver_test_ux, 10,
                                                                             class_name='button-create-resource')

            HtmlActions.click_html_element(boton_crear, class_name='button-create-resource')

            HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, 20, class_name='file-name-header')

            input_file = HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, 20, id='file_upload_start')

            HtmlActions.enviar_data_keys(input_file, path_archivo_carga, id='file_upload_start')

            ValidacionesHtml.verificar_ventana_archivo_duplicado(webdriver_test_ux)

            HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, 720, xpath='//div[@class="up-file-actions isDone"]')

            btn_cerrar_div_progreso_carga_archivo = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, 6, class_name='up-close')

            HtmlActions.webdriver_wait_invisibility_of_element_located(
                webdriver_test_ux, 20, css_selector='div.row.type-success')

            HtmlActions.verificar_elemento_html_hasta_no_existir_en_el_dom_html(
                webdriver_test_ux, time=20, css_selector='div.row.type-success')

            HtmlActions.click_html_element(btn_cerrar_div_progreso_carga_archivo, class_name='up-close')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 2, 0, True, constantes_evaluaciones_claro_drive.MSG_OUTPUT_CARGA_ARCHIVO_EXITOSO)

        except NoSuchElementException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 2, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 2, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 2, 0, False, msg_output)

        except StaleElementReferenceException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 2, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 2, tiempo_step_inicio, fecha_inicio)

        return json_eval

    @staticmethod
    def descarga_archivo_claro_drive(webdriver_test_ux: WebDriver, nombre_archivo_sin_ext: str, json_eval,
                                     ext_archivo: str):

        nombre_completo_de_la_imagen = '{}{}'.format(nombre_archivo_sin_ext, ext_archivo)
        tiempo_step_inicio = 0
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        # verifica que se haya iniciado sesion correctamente
        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_sesion(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 3,
                'No fue posible realizar la descarga del archivo. No se ingreso a la sesion de Claro Drive '
                'correctamente')

            return json_eval

        try:
            HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

            UtilsEvaluaciones.establecer_vista_de_archivos_como_lista(webdriver_test_ux)

            # establece el action para mover el mouse a un elemento html
            action = ActionChains(webdriver_test_ux)

            input_busqueda = HtmlActions.webdriver_wait_element_to_be_clickable(webdriver_test_ux, 20, id='searchbox')

            HtmlActions.enviar_data_keys(input_busqueda, nombre_completo_de_la_imagen, id='searchbox')

            HtmlActions.enviar_data_keys(input_busqueda, Keys.RETURN, id='searchbox')

            HtmlActions.webdriver_wait_presence_of_element_located(webdriver_test_ux, 20, class_name='result')

            archivo_localizado_por_descargar = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, 20, xpath='//span[@class="name-without-extension"][text()="{} "]'.format(
                    nombre_archivo_sin_ext))

            action.move_to_element(archivo_localizado_por_descargar)
            action.perform()

            lista_de_divs_de_archivos = webdriver_test_ux.find_elements_by_class_name('filename')

            if len(lista_de_divs_de_archivos) != 0:

                HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

                for div in lista_de_divs_de_archivos:
                    nombre_archivo_sin_extension_obtenido = div.find_element_by_class_name(
                        'name-without-extension').get_attribute('innerText')
                    nombre_archivo_sin_extension_obtenido = nombre_archivo_sin_extension_obtenido.strip()

                    extension_del_archivo_obtenido = webdriver_test_ux.find_element_by_class_name(
                        'ext').get_attribute('innerText')
                    extension_del_archivo_obtenido = extension_del_archivo_obtenido.strip()

                    nombre_archivo_formateado = '{}{}'.format(nombre_archivo_sin_extension_obtenido,
                                                              extension_del_archivo_obtenido)

                    if nombre_archivo_formateado == nombre_completo_de_la_imagen:
                        lista_botones = div.find_elements_by_class_name('action')

                        if len(lista_botones) > 0:

                            HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

                            boton_descarga = lista_botones[-1]

                            HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

                            HtmlActions.click_html_element(boton_descarga, class_name='action')

                            HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

                            HtmlActions.webdriver_wait_invisibility_of_element_located(
                                webdriver_test_ux, 20, css_selector='div.row.type-success')

                            HtmlActions.verificar_elemento_html_hasta_no_existir_en_el_dom_html(
                                webdriver_test_ux, time=20, css_selector='div.row.type-success')

                            break

            tiempo_step_inicio = Temporizador.obtener_tiempo_timer()

            UtilsEvaluaciones.verificar_descarga_en_ejecucion(nombre_archivo_sin_ext, ext_archivo)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 3, 0, True, constantes_evaluaciones_claro_drive.MSG_OUTPUT_DESCARGA_ARCHIVO_EXITOSO)

        except NoSuchElementException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        except StaleElementReferenceException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        except ElementNotInteractableException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 3, tiempo_step_inicio, fecha_inicio)

        return json_eval

    @staticmethod
    def borrar_archivo_claro_drive(webdriver_test_ux: WebDriver, json_eval, nombre_archivo_sin_ext: str,
                                   ext_archivo: str):

        nombre_completo_de_la_imagen = '{}{}'.format(nombre_archivo_sin_ext, ext_archivo)
        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        # verifica que se haya iniciado sesion correctamente
        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_sesion(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 4, 'No fue posible realizar el borrado del archivo. No se'
                ' ingreso a la sesion de Claro Drive correctamente')

            return json_eval

        try:
            action = ActionChains(webdriver_test_ux)

            HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

            HtmlActions.webdriver_wait_invisibility_of_element_located(
                webdriver_test_ux, 20, css_selector='div.row.type-success')

            archivo_localizado_por_descargar = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, 20, xpath='//span[@class="name-without-extension"][text()="{} "]'.format(
                    nombre_archivo_sin_ext))

            action.move_to_element(archivo_localizado_por_descargar)

            action.perform()

            lista_de_divs_de_archivos = webdriver_test_ux.find_elements_by_class_name('filename')

            if len(lista_de_divs_de_archivos) != 0:
                for div in lista_de_divs_de_archivos:
                    nombre_archivo_sin_extension_obtenido = div.find_element_by_class_name(
                        'name-without-extension').get_attribute('innerText')
                    nombre_archivo_sin_extension_obtenido = nombre_archivo_sin_extension_obtenido.strip()

                    extension_del_archivo_obtenido = webdriver_test_ux.find_element_by_class_name('ext').get_attribute(
                        'innerText')
                    extension_del_archivo_obtenido = extension_del_archivo_obtenido.strip()

                    nombre_archivo_formateado = '{}{}'.format(nombre_archivo_sin_extension_obtenido,
                                                              extension_del_archivo_obtenido)

                    if nombre_archivo_formateado == nombre_completo_de_la_imagen:
                        lista_botones = div.find_elements_by_class_name('action')

                        HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

                        if len(lista_botones) > 0:
                            boton_borrar_archivo = lista_botones[-7]

                            HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

                            HtmlActions.click_html_element(boton_borrar_archivo, class_name='action')

                            HtmlActions.verificar_modal_mensaje_de_exito(webdriver_test_ux)

                            HtmlActions.webdriver_wait_invisibility_of_element_located(
                                webdriver_test_ux, 20, css_selector='div.row.type-success')

                            HtmlActions.verificar_elemento_html_hasta_no_existir_en_el_dom_html(
                                webdriver_test_ux, time=20, css_selector='div.row.type-success')

                            break

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 4, 0, True, constantes_evaluaciones_claro_drive.MSG_OUTPUT_BORRADO_ARCHIVO_EXITOSO)

        except NoSuchElementException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        except StaleElementReferenceException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        except ElementNotInteractableException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 4, tiempo_step_inicio, fecha_inicio)

        return json_eval

    @staticmethod
    def cerrar_sesion_claro_drive(webdriver_test_ux: WebDriver, json_eval):
        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        # verifica que se haya iniciado sesion correctamente
        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_sesion(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 5, 'No fue posible realizar el cierre de sesion. No se '
                'ingreso a la sesion de Claro Drive correctamente')

            return json_eval

        try:
            HtmlActions.webdriver_wait_until_not_presence_of_element_located(
                webdriver_test_ux, 20, css_selector='div.row.type-success')

            boton_cerrar_sesion = HtmlActions.webdriver_wait_invisibility_of_element_located(
                webdriver_test_ux, 20, xpath='//li[@data-id="logout"]/a')

            link_cierre_de_sesion = boton_cerrar_sesion.get_attribute("href")

            webdriver_test_ux.get(link_cierre_de_sesion)

            tiempo_step_inicio = Temporizador.obtener_tiempo_timer()

            HtmlActions.webdriver_wait_presence_of_element_located(webdriver_test_ux, 20, id='login')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 5, 0, True, constantes_evaluaciones_claro_drive.MSG_OUTPUT_CIERRE_SESION_EXITOSO)

        except NoSuchElementException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        except ElementNotInteractableException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        except StaleElementReferenceException as e:
            msg_output = constantes_evaluaciones_claro_drive.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 5, tiempo_step_inicio, fecha_inicio)

        return json_eval
