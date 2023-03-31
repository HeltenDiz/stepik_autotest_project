
import re


class BaseClass:

    def read_title(self, element):
        """Метод возвращает текст элемента"""
        value_text = element.text
        return value_text

    def leave_numbers_1(self, string):
        """Метод возвращает вещественные числа из строки"""

        nums = re.findall(r'\d*\.\d+|\d+', string)
        if nums:
            nums = float(nums[0])

        print(nums)
        return nums

    def leave_numbers_2(self, string):
        """Метод возвращает вещественные числа из строки"""

        nums = ''
        for i in string:
            if i.isdigit() or i == '.':
                nums = nums + i
        print(nums)
        return nums


class CustomList(Element):
    """Класс для работы с разнообразными списками

    Для того, что бы задать список в locators нужно указать локатор,
    по которому будут находиться все элементы списка
    """

    def __str__(self) -> str:
        return 'произвольный список'

    def __iter__(self):
        return ListIterator(self, self.size)

    def __contains__(self, text: str) -> bool:
        """Вхождение текста"""

        return self.item(contains_text=text).is_displayed


class Element:
    """Базовый класс для всех элементов

    | Содержит в себе методы, которые актуальны для большинства наследников.
    | При этом сам может быть использован для моделирования в коде объектов,
    | которые не подходят ни под одного наследника. Типичные примеры:

    * блок страницы с картинкой
    * div, появления которого нужно просто дождаться

    :param how: локатор нахождения webelement
    :param locator: локатор нахождения webelement
    :param rus_name: русское наименование элемента
    """

    IGNORE_ATTRS = ('region', 'parent')

    def __str__(self) -> str:
        return 'элемент'

    def __repr__(self):
        return f'{self.__class__}\nPO path: {self.get_po_path()}\n{self.locator_as_str()}'

    def __init__(self, how: str, locator: str, rus_name: str = '', **kwargs):
        """Описание элемента

        :param how стратегия поиска
        :param locator селектор
        :param rus_name русское имя элемента
        :param absolute_position абсолютное позиционирование (ингнорирование иерархии)
        :param driver WebDriver
        """
        self.how = check_strategy_search(how)
        self.locator = format_locator(locator)
        kwargs.pop('name', '')
        self.rus_name = get_log_element(rus_name=rus_name)
        self._str: Optional[str] = None

        self._absolute_position = kwargs.pop('absolute_position', False)
        self.parent = kwargs.get('parent')  # родитель, subclass Element
        self.region = kwargs.get('region')  # в атрибут сохряется регион из которого зовется элемент
        self.driver: WebDriver = kwargs.pop('driver', None)

        self._find_element: Optional[Callable] = None
        self._kwargs_tuple = tuple(kwargs.items())
        if self.driver:  # когда driver передали через параметры инициализации, вне класса Region
            self.init(self.driver)