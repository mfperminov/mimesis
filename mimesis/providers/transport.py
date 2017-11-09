from mimesis.data import AIRPLANES, CARS, TRUCKS
from mimesis.providers.base import BaseProvider
from mimesis.utils import custom_code


class Transport(BaseProvider):
    """Class that provides dummy data about transport."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def truck(self, model_mask: str = '#### @@') -> str:
        """Generate a truck model.

        :param str model_mask: Mask of truck model. Here '@' is a \
        placeholder of characters and '#' is a placeholder of digits.
        :return: Dummy truck model.
        :rtype: str

        :Example:
            Caledon-966O.
        """
        model = custom_code(mask=model_mask)
        truck = self.random.choice(TRUCKS)
        return '%s-%s' % (truck, model)

    def car(self) -> str:
        """Get a random vehicle.

        :return: A vehicle.
        :rtype: str

        :Example:
            Tesla Model S.
        """
        return self.random.choice(CARS)

    def airplane(self, model_mask: str = '###') -> str:
        """Generate a dummy airplane model.

        :param str model_mask: Mask of truck model. Here '@' is a \
        placeholder of characters and '#' is a placeholder of digits.
        :return: Airplane model.
        :rtype: str

        :Example:
            Boeing 727.
        """
        model = custom_code(mask=model_mask)
        plane = self.random.choice(AIRPLANES)
        return '%s %s' % (plane, model)
