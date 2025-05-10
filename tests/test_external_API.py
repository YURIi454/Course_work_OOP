from unittest.mock import Mock, patch

from src.external_API import HeadHunter, WorkRussia


@patch("requests.get")
def test_cls_hh_api(mock_response) -> None:
    """Мок - тест , API , класса HeadHunter"""

    mock_response = Mock()
    mock_response.status_code = 200
    hh = HeadHunter()
    hh.return_vacancies("")


@patch("requests.get")
def test_cls_wr_api(mock_response) -> None:
    """Мок - тест , API , класса WorkRussia"""

    mock_response = Mock()
    mock_response.status_code = 200
    wr = WorkRussia()
    wr.return_vacancies("")
