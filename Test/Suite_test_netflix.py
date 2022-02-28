# LIBRERÍAS
import sys
sys.path.append(r"C:\Prueba_Stech")
import unittest
import HtmlTestRunner
# ARCHIVOS DONDE SE ENCUENTRAN LOS TEST
import test_netflix

# INSTANCIA DE LOADER Y SUIT
loader = unittest.TestLoader()
suit = unittest.TestSuite()

# AGREGADO DE TESTS A LA SUIT
suit.addTest(test_netflix.NetflixTest("test_validar_titulo_test"))
suit.addTest(test_netflix.NetflixTest("test_start_session_page_test"))
suit.addTest(test_netflix.NetflixTest("test_login_to_netflix_error_test"))
suit.addTest(test_netflix.NetflixTest("test_fake_email_test"))
suit.addTest(test_netflix.NetflixTest("test_print_tags_test"))

# RUNNER Y REPORTE HTML
h = HtmlTestRunner.HTMLTestRunner(
    combine_reports=True, report_name="Reporte NetflixTest", add_timestamp=False, verbosity=2).run(suit)
