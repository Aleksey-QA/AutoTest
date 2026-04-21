import generate_schedule
import pytest

@pytest.mark.parametrize("num, zon, res", [(2, "Europe/Helsinki", [('Su', '08/02', 'Closed'), ('Mo', '09/02', '00:05–22:55')]),
                                           (3, "Europe/Helsinki", [('Su', '08/02', 'Closed'), ('Mo', '09/02', '00:05–22:55'), ('Tu', '10/02', '00:05–22:55')]),
                                           (4, "Europe/Helsinki", [('Su', '08/02', 'Closed'), ('Mo', '09/02', '00:05–22:55'), ('Tu', '10/02', '00:05–22:55'), ('We', '11/02', '00:05–22:55')]),
                                           (0, "Europe/Helsinki", []),
                                           (-1, "Europe/Helsinki", []),
                                           (2, "Europe/Minsk", [('Su', '08/02', 'Closed'), ('Mo', '09/02', '00:05–22:55')]),
                                           (2, "America/Los_Angeles", [('Su', '08/02', 'Closed'), ('Mo', '09/02', '00:05–22:55')]
                                            )])
def test_generate_week_schedule(num, zon, res):
    assert generate_schedule.generate_week_schedule(num, zon) == res
