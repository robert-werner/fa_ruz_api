import pendulum
from fa_ruz_api.base import RuzEndpoint


class Schedule(RuzEndpoint):
    """
    Schedule RUZ endpoint class.
    """

    def __init__(self):
        super().__init__(endpoint='schedule')

    def _schedule_(self,
                   entity_id,
                   entity_type,
                   begin_date=None,
                   end_date=None,
                   language=1):
        """
        Internal schedule requestor.
        Should not be used directly.
        """
        if begin_date is None or end_date is None:
            begin_date = pendulum.now().format('YYYY.MM.DD')
            end_date = begin_date
        schedule = self._request_(endpoint=f'schedule/{entity_type}/{entity_id}', start=begin_date, finish=end_date,
                                  lng=language)
        return schedule

    def group_schedule(self,
                       group_id,
                       begin_date,
                       end_date,
                       language=1):
        """
        Requests group's schedule by its internal RUZ id.
        """
        return self._schedule_(group_id, 'group', begin_date, end_date, language)

    def lecturer_schedule(self,
                          lecturer_id,
                          begin_date,
                          end_date,
                          language=1):
        """
        Requests lecturer's schedule by its internal RUZ id.
        """
        return self._schedule_(lecturer_id, 'person', begin_date, end_date, language)

    def classroom_schedule(self,
                           classroom_id,
                           begin_date,
                           end_date,
                           language=1):
        """
        Requests classroom's schedule by its internal RUZ id.
        """
        return self._schedule_(classroom_id, 'auditorium', begin_date, end_date, language)

    def building_schedule(self,
                          building_id,
                          begin_date,
                          end_date,
                          language=1):
        """
        Requests building's schedule by its internal RUZ id.
        """
        return self._schedule_(building_id, 'building', begin_date, end_date, language)
