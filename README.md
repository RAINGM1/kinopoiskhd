# Kinopoiskhd

[![PyPI version](https://img.shields.io/pypi/v/kinopoiskрhd.svg)](https://pypi.python.org/pypi/kinopoiskhd)

This package using unofficial API to kinopoisk.ru website.

## Installation

To install the latest version using pip:

    $ pip install kinopoiskhd

## Example usage

Get token from "https://kinopoiskapiunofficial.tech/user"

Search movies by keywords:

    >>> from kinopoiskhd import Searchbykeyword
    >>> hueta = Searchbykeyword('Звёздные Войны', token)
    >>> hueta = hueta.searchbykeyword()
    >>> print(hueta)
    <Response [200]>
    >>> print(hueta.json())
    json data

Search movie by ID:

    >>> from kinopoiskhd import Searchbyid
    >>> hueta = Searchbyid(6695, token)
    >>> hueta = hueta.searchbyid()
    >>> print(hueta)
    <Response [200]>
    >>> print(hueta.json())
    json data
    
Search data by ID:

    >>> from kinopoiskhd import Searchdatabyid
    >>> hueta = Searchdatabyid(6695, token)
    >>> print(hueta.filmTitleru)
    >>> print(hueta.filmTitleen)
    >>> print(hueta.filmMainurlru)
    >>> print(hueta.filmMainurlen)
    >>> print(hueta.posterUrl)
    >>> print(hueta.posterUrlPreview)
    >>> print(hueta.year)
    >>> print(hueta.filmLength)
    >>> print(hueta.slogan)
    >>> print(hueta.description)
    >>> print(hueta.types)
    >>> print(hueta.ratingMpaa)
    >>> print(hueta.ratingAgeLimits)
    >>> print(hueta.premiereRu)
    >>> print(hueta.distributors)
    >>> print(hueta.premiereWorld)
    >>> print(hueta.premiereDigital)
    >>> print(hueta.premiereWorldCountry)
    >>> print(hueta.premiereDvd)
    >>> print(hueta.premiereBluRay)
    >>> print(hueta.distributorRelease)
    >>> print(hueta.countries)
    >>> print(hueta.genres)
    >>> print(hueta.facts)

    Звёздные войны: Эпизод 1 – Скрытая угроза
    Star Wars: Episode I - The Phantom Menace
    http://www.kinopoisk.ru/film/6695/
    http://www.kinopoisk.ru/film/6695/
    https://kinopoiskapiunofficial.tech/images/posters/kp/6695.jpg
    https://kinopoiskapiunofficial.tech/images/posters/kp_small/6695.jpg
    1999
    2:16
    У каждой саги есть начало
    Мирная и процветающая планета Набу. Торговая федерация, не желая платить налоги, вступает в прямой конфликт с королевой Амидалой, правящей на планете, что приводит к войне. На стороне королевы и республики в ней участвуют два рыцаря-джедая: учитель и ученик, Квай-Гон-Джин и Оби-Ван Кеноби...
    FILM
    PG
    0
    1999-07-29
    Гемини, Двадцатый Век Фокс СНГ
    1999-05-16
    None
    США
    2010-12-09
    2011-09-15
    Двадцатый Век Фокс СНГ
    США
    ['боевик', 'фантастика', 'фэнтези']
    ['Первой в ходе съёмок была снята сцена разговора между Дарт Сидиусом и Дарт Молом.', 'Сцена битвы на световых мечах между Дарт Молом и Оби-Ваном с Квай-Гоном снималась на протяжении месяца. Это первая схватка такого рода, в которой принимали участие более двух джедаев или ситхов.', 'Звук трепещущих крыльев торговца Уотто был достигнут звукооператором Беном Берттом в результате открывания и закрывания обычного зонтика.', 'До съёмок в роли королевы Амидалы Натали Портман не видела ни одного фильма из оригинальной трилогии «Звёздных войн».', 'Натали Портман пропустила мировую премьеру «Скрытой угрозы» по причине подготовки к сессии в университете.', 'София Коппола и Кира Найтли получили короткие роли служанок Падме в фильме. Фактически поразительное внешнее сходство Натали Портман и Киры Найтли стало залогом последующей актёрской карьеры последней.', 'Из-за высокого роста Лиама Нисона декораторам пришлось потратить ещё 150 000 долларов на новые декорации, в которых актёр смог бы уместиться.', 'На пресс-конференции, посвящённой выходу фильма «Звездные войны: Эпизод 3 – Месть Ситхов» (2005) на DVD, директор по анимации Роб Коулмэн объявил, что готовится обновлённая версия «Скрытой угрозы», благодаря чему первый эпизод станет последним фильмом саги, в котором кукольного Йоду заменят генерированным при помощи цифровых технологий.', 'В титрах Джабба Хатт, открывающий гонки на подах, обозначен «Джабба Хатт в роли самого себя». Одновременно в титрах не указывается, что Иен МакДермид играет Дарта Сидиуса.', '«Скрытая угроза» — единственный фильм «Звёздных войн», в котором представлена уникальная способность джедаев к ускорению. ', 'Передатчик (комлинк) Квай-Гон Джина представляет собой слегка модифицированную бритву «Жиллетт Сенсор Эксель».   ', 'После прокрутки всех титров в конце фильма слышно зловещее дыхание Дарта Вейдера. ', 'Образы всех гунганов были созданы на движке Джа-Джа Бинкса.', 'Во время битвы гунганов с войсками Федерации мелькает дроид с серийным номером «1138» на спине: это число входило в название первого полнометражного фильма Джорджа Лукаса, 
    называвшегося «Галактика ТНХ-1138» (1971). Один из кораблей, пролетающих над Корусантом за миг до разговора Дарт Сидиуса и Дарт Мола, идентичен «Дискавери» из фильма «2001 год: Космическая одиссея» (1968). Спасательная капсула этого же корабля видна в сцене разговора между Квай-Гоном и Уотто на заднем плане среди прочих ржавых деталей в «лавке» Уотто на Татуине.', 'В сцене заседания Галактического Сената можно разобрать несколько делегаций, в том числе вуки и группу инопланетян, напоминающих знаменитого E.T. из фильма Стивена Спилберга «Инопланетянин» (1982).', 'В ранних версиях сценария планета королевы Амидалы называлась Утапау, но в итоге это название отошло к планете, где Оби-Ван сражается с генералом Гривусом в фильме «Звездные войны: Эпизод 3 – Месть Ситхов» (2005).', 'Единственная сцена в фильме, в которой не используются визуальные эффекты — это сцена заполнения газом комнаты встреч в начале фильма. ', 'Во время съемок сражений Юэн МакГрегор часто непроизвольно изображал звук светового меча.', 'Изначально Мэйс Винду (Сэмюэл Л. Джексон) должен был быть инопланетянином.', '«Падме» с санскрита означает «лотос». ', 'Дарт Мол за весь фильм моргает всего пару раз. Это было вызвано тем, что сыгравшему его Рэю Парку было трудно моргать в контактных линзах, поэтому Парк предложил идею 
    о злодее, который никогда не моргает.', 'На роль юного Энакина Скайуокера пробовались Хэйли Джоэл Осмент и Майкл Ангарано.', 'Имя «Джа-Джа Бинкс» придумал сын Лукаса.', 'На боевых дисплеях ТФ, во время атаки гунганов на войска торговой федерации, показана игра 
    Star Wars: Galactic Battlegrounds.']

## Contributors

[RANIGM](http://github.com/RAINGM1)
