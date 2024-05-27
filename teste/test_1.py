import pytest


class Test1:

    @pytest.mark.parametrize('all_browsers', ['chrome', 'safari', 'firefox'])
    def test_click_login_btn(self, run_all_browser):
        login_page = run_all_browser
        # Passos do teste
        login_page.click_login_button()

        assert login_page.is_url_login(), 'URL incorreta!'
        assert login_page.has_message_login_message_error(), 'Messagem de erro incorreta!'