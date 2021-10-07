from fa_ruz_api.base import RuzEndpoint
from fa_ruz_api.letterflip import letterflip


class Search(RuzEndpoint):

    def __init__(self):
        super().__init__(endpoint='search')

    def _find_entity_(self, entity_name, entity_type, entity_attribute, flip_letter=False):
        """
        The common method for finding entities.
        """
        if flip_letter:  # Monkey-patch flag for flipping the same looking Russian and Latin letters
            entity_name = letterflip(entity_name)
        entity_list = self._request_(term=entity_name, type=entity_type)
        if not entity_list:
            return None
        for entity in entity_list:
            if entity_name.casefold() in entity[entity_attribute].casefold():
                return entity
        return False

    def find_group(self, group_name, flip_letter=True):
        """
        Sees whether group exists. Returns group's internal RUZ entry, otherwise returns False.
        """
        return self._find_entity_(group_name, 'group', 'label', flip_letter)

    def find_lecturer(self, lecturer_name, flip_letter=False):
        """
        Sees whether lecturer exists. Returns lecturer's internal RUZ entry, otherwise returns False.
        """
        return self._find_entity_(lecturer_name, 'person', 'label', flip_letter)

    def find_classroom(self, classroom_name, flip_letter=True):
        """
        Sees whether classroom exists. Return classroom's internal RUZ entry, otherwise returns False.

        It is important that the classroom exact information is contained in description.
        """
        return self._find_entity_(classroom_name, 'auditorium', 'description', flip_letter)

    def find_building(self, building_name, flip_letter=True):
        """
        Sees whether building exists. Return building's internal RUZ entry, otherwise returns False.
        """
        return self._find_entity_(building_name, 'building', 'label', flip_letter)
