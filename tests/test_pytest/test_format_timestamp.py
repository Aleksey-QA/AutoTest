from datetime import datetime, timedelta, timezone
import pytest
# Создать фикстуру которая будет генерирует timestamp
# Создать автотесты которые будут проверять что функция `format_timestamp`
# правильно форматирует данные
# пример
# '2024-01-01 15:00:00'
# '01.01.2024 15:00'
# '15:00:00'
# '2024-01-01'
# * проверять не на совпадение строки, а по regexp
@pytest.fixture()
def get_data():
    base_dt = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    base_ts_ms = int(base_dt.timestamp() * 1000)
    return base_ts_ms

print(get_data)

def format_timestamp(timestamp_ms, format_type="standard", offset_hours=0):
    timestamp_seconds = timestamp_ms / 1000
    dt = datetime.fromtimestamp(timestamp_seconds)
    corrected_dt = dt + timedelta(hours=offset_hours)
    formats = {
        "standard": "%Y-%m-%d %H:%M:%S",
        "short": "%d.%m.%Y - %H:%M",
        "time_only": "%H:%M:%S",
        "date_only": "%Y-%m-%d",
    }

    return corrected_dt.strftime(formats.get(format_type))

def test_format_timestamp(get_data):
    print(f"вызвали фикстуру {get_data}")
    base_dt = get_data

    result = format_timestamp(base_dt, "short")
    assert result == "01.01.2024 - 15:00"

