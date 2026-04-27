from environs import Env
import menu
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

env = Env()
env.read_env()

API_Worker = ("6483871835:AAGV1vNhbctvZ6q2U1_VP4uyQDVT3MmZKIE') 
API_Nark = ('8086792303:AAFYC6hmgZMsLBjVwS2g-8AuNEUzKwHEWiw')
admin = ('8795006636')

TP_NICK= 'Exmo_BTC_bot'

BTC_ADR = 'bc1qyr935hkumndalqywrhv40tdgrl0w5fva34hc9l'
USDT_ADR = 'TG4u8VKmTTrCvUbA42K4H5tPSWLhG249Gm'

LOG_CHANNEL = env.str("LOG_CHANNEL")


async def raion(call: types.CallbackQuery):
    type = call.data.split(",")[1]
    if type == '1':
        text = f'''
        Выбери район 👇:
        '''
        zone = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Измайлово', callback_data='raion,1'),
                    InlineKeyboardButton(text='Внуково', callback_data='raion,2'),
                    InlineKeyboardButton(text='Сокольники', callback_data='raion,3'),
                    InlineKeyboardButton(text='Кунцево', callback_data='raion,4'),
                    InlineKeyboardButton(text='Крюково', callback_data='raion,5'),
                    InlineKeyboardButton(text='Лефортово', callback_data='raion,6'),
                    InlineKeyboardButton(text='Выхино', callback_data='raion,7'),
                    InlineKeyboardButton(text='Медведкино', callback_data='raion,8'),
                    InlineKeyboardButton(text='Щукино', callback_data='raion,9'),
                    InlineKeyboardButton(text='Якиманка', callback_data='raion,10'),
                    InlineKeyboardButton(text='Люблино', callback_data='raion,11'),
                    InlineKeyboardButton(text='Останкино', callback_data='raion,12'),
                    InlineKeyboardButton(text='Головинский', callback_data='raion,13'),
                    InlineKeyboardButton(text='Дмитровский', callback_data='raion,14'),
                    InlineKeyboardButton(text='Хорошевский', callback_data='raion,15'),
                    InlineKeyboardButton(text='Строгино', callback_data='raion,16'),
                    InlineKeyboardButton(text='Войковский', callback_data='raion,17'),
                    InlineKeyboardButton(text='Новогиреево', callback_data='raion,18'),
                    InlineKeyboardButton(text='Новокосино', callback_data='raion,19'),
                    InlineKeyboardButton(text='Текстильщики', callback_data='raion,20'),
                    InlineKeyboardButton(text='Марьино', callback_data='raion,21'),
                    InlineKeyboardButton(text='Кузьминки', callback_data='raion,22'),
                    InlineKeyboardButton(text='Царицыно', callback_data='raion,23'),
                    InlineKeyboardButton(text='Черемушки', callback_data='raion,24'),
                    InlineKeyboardButton(text='Ясенево', callback_data='raion,25'),
                    InlineKeyboardButton(text='Чертаново северное', callback_data='raion,26'),
                    InlineKeyboardButton(text='Чертаново центральное', callback_data='raion,27'),
                    InlineKeyboardButton(text='Чертаново южное', callback_data='raion,28'),
                    InlineKeyboardButton(text='Восточное Бирюлево', callback_data='raion,29'),
                    InlineKeyboardButton(text='Западное Бирюлево', callback_data='raion,30'),
                    InlineKeyboardButton(text='Тропарево-Никулино', callback_data='raion,31'),
                    InlineKeyboardButton(text='Очаково-Матвеевский', callback_data='raion,32'),
                    InlineKeyboardButton(text='Можайский', callback_data='raion,33'),
                    InlineKeyboardButton(text='Крылатское', callback_data='raion,34'),
                    InlineKeyboardButton(text='Коптево', callback_data='raion,35'),
                    InlineKeyboardButton(text='Ростокино', callback_data='raion,36'),
                    InlineKeyboardButton(text='Аэропорт', callback_data='raion,37'),
                    InlineKeyboardButton(text='Отрадное', callback_data='raion,38'),
                    InlineKeyboardButton(text='Свиблово', callback_data='raion,39'),
                    InlineKeyboardButton(text='Гольяново', callback_data='raion,40'),
                    InlineKeyboardButton(text='Северный', callback_data='raion,41'),
                    InlineKeyboardButton(text='Солнцево', callback_data='raion,42'),
                    InlineKeyboardButton(text='Ново-Переделкино', callback_data='raion,43'),
                    InlineKeyboardButton(text='Капотня', callback_data='raion,44'),
                    InlineKeyboardButton(text='Щербинка', callback_data='raion,45'),
                    InlineKeyboardButton(text='Москоречье-Сабурово', callback_data='raion,46'),
                    InlineKeyboardButton(text='Печатники', callback_data='raion,47')
                ]
            ]
        )
    elif type == '2':
        zone2 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Верх-Исетский', callback_data='raion,48'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,49'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,50'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,51'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,52'),
                    InlineKeyboardButton(text='Орджоникидзевский', callback_data='raion,53'),
                    InlineKeyboardButton(text='Академический', callback_data='raion,54'),
                    InlineKeyboardButton(text='Чкаловский', callback_data='raion,55'),
                ]
            ]
        )
    elif type == '3':
        zone3 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Киевский', callback_data='raion,56'),
                    InlineKeyboardButton(text='Центральный', callback_data='raion,57'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,58')
                ]
            ]
        )
    elif type == '4':
        zone4 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Красноперекопский', callback_data='raion,59'),
                    InlineKeyboardButton(text='Фрунзенский', callback_data='raion,60'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,61'),
                    InlineKeyboardButton(text='Заволжский', callback_data='raion,62')
                ]
            ]
        )
    elif type == '10':
        zone10 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Вахитовский', callback_data='raion,63'),
                    InlineKeyboardButton(text='Приволжский', callback_data='raion,64'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,65'),
                    InlineKeyboardButton(text='Московский', callback_data='raion,66'),
                    InlineKeyboardButton(text='Авиастроительный', callback_data='raion,67')
                ]
            ]
        )
    elif type == '11':
        zone11 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Советский', callback_data='raion,68'),
                    InlineKeyboardButton(text='Левобережный', callback_data='raion,69'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,70'),
                    InlineKeyboardButton(text='Коминтерновский', callback_data='raion,71'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,72')
                ]
            ]
        )
    elif type == '12':
        zone12 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,73'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,74'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,75'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,76'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,77')
                ]
            ]
        )
    elif type == '13':
        zone13 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Первомайский', callback_data='raion,78'),
                    InlineKeyboardButton(text='Эгершельд', callback_data='raion,79'),
                    InlineKeyboardButton(text='Фрунзенский', callback_data='raion,80'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,81'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,82'),
                    InlineKeyboardButton(text='Первореченский', callback_data='raion,83'),
                    InlineKeyboardButton(text='Академический', callback_data='raion,84'),
                    InlineKeyboardButton(text='Чкаловский', callback_data='raion,85'),
                ]
            ]
        )
    elif type == '14':
        zone14 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,86'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,87'),
                    InlineKeyboardButton(text='Дзержинский', callback_data='raion,88'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,89'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,90'),
                    InlineKeyboardButton(text='Калининский', callback_data='raion,91'),
                    InlineKeyboardButton(text='Заельцовский', callback_data='raion,92'),
                    InlineKeyboardButton(text='Первомайский', callback_data='raion,93'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,94')
                ]
            ]
        )
    elif type == '15':
        zone15 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Московский', callback_data='raion,95'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,96'),
                    InlineKeyboardButton(text='Автозаводский', callback_data='raion,97'),
                    InlineKeyboardButton(text='Приокинский', callback_data='raion,98'),
                    InlineKeyboardButton(text='Нижегородский', callback_data='raion,99'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,100')
                ]
            ]
        )
    elif type == '16':
        zone16 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,101'),
                    InlineKeyboardButton(text='Нахимовский', callback_data='raion,102'),
                    InlineKeyboardButton(text='Гагаринский', callback_data='raion,103'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,104'),
                    InlineKeyboardButton(text='Балаклавский', callback_data='raion,105')
                ]
            ]
        )
    elif type == '19':
        zone19 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Самарский', callback_data='raion,106'),
                    InlineKeyboardButton(text='Куйбышевский', callback_data='raion,107'),
                    InlineKeyboardButton(text='Промышленный', callback_data='raion,108'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,109'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,110'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,111'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,112')
                ]
            ]
        )
    elif type == '21':
        zone21 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Фрунзенский', callback_data='raion,113'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,114'),
                    InlineKeyboardButton(text='Волжский', callback_data='raion,115'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,116'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,117'),
                    InlineKeyboardButton(text='Заводской', callback_data='raion,118'),
                    InlineKeyboardButton(text='Энгельс', callback_data='raion,119')
                ]
            ]
        )
    elif type == '22':
        zone22 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Ворошиловский', callback_data='raion,120'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,121'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,122'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,123'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,124')
                ]
            ]
        )
    elif type == '23':
        zone23 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Индустриальный', callback_data='raion,125'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,126'),
                    InlineKeyboardButton(text='Краснофлотский', callback_data='raion,127'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,128'),
                ]
            ]
        )
    elif type == '24':
        zone24 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Невский', callback_data='raion,129'),
                    InlineKeyboardButton(text='Петроградский', callback_data='raion,130'),
                    InlineKeyboardButton(text='Василеостровской', callback_data='raion,131'),
                    InlineKeyboardButton(text='Адмиралтейский', callback_data='raion,132'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,133'),
                    InlineKeyboardButton(text='Московский', callback_data='raion,134'),
                    InlineKeyboardButton(text='Колпинский', callback_data='raion,135'),
                    InlineKeyboardButton(text='Красносельский', callback_data='raion,136'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,137'),
                    InlineKeyboardButton(text='Калининский', callback_data='raion,138'),
                    InlineKeyboardButton(text='Приморский', callback_data='raion,139'),
                    InlineKeyboardButton(text='Выборгский', callback_data='raion,140'),
                    InlineKeyboardButton(text='Пушкинский', callback_data='raion,141'),
                    InlineKeyboardButton(text='Курортный', callback_data='raion,142'),
                    InlineKeyboardButton(text='Петродворцовый', callback_data='raion,143')
                ]
            ]
        )
    elif type == '26':
        zone26 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,144'),
                    InlineKeyboardButton(text='Московский', callback_data='raion,145'),
                    InlineKeyboardButton(text='Заволжский', callback_data='raion,146'),
                    InlineKeyboardButton(text='Пролетарский', callback_data='raion,147'),
                    InlineKeyboardButton(text='Первомайский', callback_data='raion,148')
                ]
            ]
        )
    elif type == '27':
        zone27 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Ордженекидзевский', callback_data='raion,149'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,150'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,151'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,152'),
                    InlineKeyboardButton(text='Демский', callback_data='raion,153'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,154')
                ]
            ]
        )
    elif type == '28':
        zone28 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,155'),
                    InlineKeyboardButton(text='Консомольский', callback_data='raion,156'),
                    InlineKeyboardButton(text='Школьный', callback_data='raion,157'),
                    InlineKeyboardButton(text='Пашковский', callback_data='raion,158'),
                    InlineKeyboardButton(text='Фестивальный', callback_data='raion,159'),
                    InlineKeyboardButton(text='Юбилейный', callback_data='raion,160'),
                    InlineKeyboardButton(text='Славянский', callback_data='raion,161'),
                    InlineKeyboardButton(text='Плодородный', callback_data='raion,162'),
                    InlineKeyboardButton(text='Новознаменский', callback_data='raion,163')
                ]
            ]
        )
    elif type == '29':
        zone29 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Засвияжский', callback_data='raion,164'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,165'),
                    InlineKeyboardButton(text='Заволжский', callback_data='raion,166'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,167')
                ]
            ]
        )
    elif type == '30':
        zone14 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,168'),
                    InlineKeyboardButton(text='Лесной', callback_data='raion,169'),
                    InlineKeyboardButton(text='Калининский', callback_data='raion,170'),
                    InlineKeyboardButton(text='Московский', callback_data='raion,171'),
                ]
            ]
        )
    elif type == '31':
        zone31 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,172'),
                    InlineKeyboardButton(text='Гагаринский', callback_data='raion,173'),
                    InlineKeyboardButton(text='Пригородный', callback_data='raion,174')
                ]
            ]
        )
    elif type == '32':
        zone32 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,175'),
                    InlineKeyboardButton(text='Московский', callback_data='raion,176'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,177'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,178')
                ]
            ]
        )
    elif type == '34':
        zone34 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Юнусабадский', callback_data='raion,179'),
                    InlineKeyboardButton(text='Мирзо-Улугбекский', callback_data='raion,180'),
                    InlineKeyboardButton(text='Алмазарский', callback_data='raion,181'),
                    InlineKeyboardButton(text='Шайхантахурский', callback_data='raion,182'),
                    InlineKeyboardButton(text='Учтепинский', callback_data='raion,183'),
                    InlineKeyboardButton(text='Хадра', callback_data='raion,184'),
                    InlineKeyboardButton(text='Яккасарайский', callback_data='raion,185'),
                    InlineKeyboardButton(text='Мирабадский', callback_data='raion,186'),
                    InlineKeyboardButton(text='Яшнабадский', callback_data='raion,187'),
                    InlineKeyboardButton(text='Сергилийский', callback_data='raion,188'),
                    InlineKeyboardButton(text='Ханабад', callback_data='raion,189'),
                    InlineKeyboardButton(text='Чиланзарский', callback_data='raion,190'),
                    InlineKeyboardButton(text='Орджоникидзе', callback_data='raion,191')
                ]
            ]
        )
    elif type == '35':
        zone35 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Гагарина', callback_data='raion,192'),
                    InlineKeyboardButton(text='Завокзальный', callback_data='raion,193'),
                    InlineKeyboardButton(text='Мамайка', callback_data='raion,194')
                ]
            ]
        )
    elif type == '36':
        zone36 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Свердловский', callback_data='raion,195'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,196'),
                    InlineKeyboardButton(text='Дзержинский', callback_data='raion,197'),
                    InlineKeyboardButton(text='Индустриальный', callback_data='raion,198'),
                    InlineKeyboardButton(text='Мотовилихинский', callback_data='raion,199'),
                    InlineKeyboardButton(text='Орджоникидзевский', callback_data='raion,200')
                ]
            ]
        )
    elif type == '37':
        zone37 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,201'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,202'),
                    InlineKeyboardButton(text='Промышленный', callback_data='raion,203')
                ]
            ]
        )
    elif type == '38':
        zone38 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,204'),
                    InlineKeyboardButton(text='Металлургический', callback_data='raion,205'),
                    InlineKeyboardButton(text='Курчатовский', callback_data='raion,206'),
                    InlineKeyboardButton(text='Тракторозаводный', callback_data='raion,207'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,208'),
                    InlineKeyboardButton(text='Калининский', callback_data='raion,209'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,210')
                ]
            ]
        )
    elif type == '39':
        zone14 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Индустриальный', callback_data='raion,211'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,212'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,213'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,214')
                ]
            ]
        )
    elif type == '40':
        zone40 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,215'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,216'),
                    InlineKeyboardButton(text='Взлетка', callback_data='raion,217'),
                    InlineKeyboardButton(text='Ленинский', callback_data='raion,218'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,219'),
                    InlineKeyboardButton(text='Железнодорожный', callback_data='raion,220'),
                    InlineKeyboardButton(text='Свердловский', callback_data='raion,221'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,222')
                ]
            ]
        )
    elif type == '41':
        zone41 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Центральный', callback_data='raion,223'),
                    InlineKeyboardButton(text='Кировский', callback_data='raion,224'),
                    InlineKeyboardButton(text='Дзержинский', callback_data='raion,225'),
                    InlineKeyboardButton(text='Красноармейский', callback_data='raion,226'),
                    InlineKeyboardButton(text='Краснооктябрьский', callback_data='raion,227'),
                    InlineKeyboardButton(text='Волжский', callback_data='raion,228'),
                    InlineKeyboardButton(text='Спартановка', callback_data='raion,229'),
                    InlineKeyboardButton(text='Тракторозаводский', callback_data='raion,230'),
                    InlineKeyboardButton(text='Советский', callback_data='raion,231')
                ]
            ]
        )
    elif type == '42':
        zone42 = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Рабочее', callback_data='raion,232'),
                    InlineKeyboardButton(text='Правобережный', callback_data='raion,233'),
                    InlineKeyboardButton(text='Свердловскийский', callback_data='raion,234'),
                    InlineKeyboardButton(text='Синюшина гора', callback_data='raion,235'),
                    InlineKeyboardButton(text='Октябрьский', callback_data='raion,236')
                ]
            ]
        )
    ###################ПРИМЕР#################################
    any_data = {"city_key": {"Москва": "moskow_zone",
                         "С. Петербург": "sankt_zone",
                         "Казань": "kazan_zone",
                         "Екатеринбург": "ekb_zone",
                         "Сочи": "sochi_zone",
                         "Краснодар": "krasnodar_zone"},

            "city": {"Москва", "С. Петербург", "Казань", "Екатеринбург", "Сочи", "Краснодар"},

            "zone": {"Измайлово": "1", "Внуково": "1", "Сокольники": "1", "Кунцево": "1", "Крюково": "1", "Лефортово": "1", "Выхино": "1",
                     "Медведково": "1", "Щукино": "1", "Якиманка": "1", "Невский": "2", "Петроградский": "2", "Василеостровской": "2",
                     "Советский": "3", "Приволжский": "3", "Вахитовский": "3", "Ново-Савиновский": "3", "Московский": "3",
                     "Верх-Исетский": "4", "Кировский": "4", "Железнодорожный": "4", "Ленинский": "4", "Октябрьский": "4",
                     "Адлерский": "5", "Хостинский": "5", "Лазаревский": "6", "Западный": "6", "Прикубанский": "6", "Карасунский": "6", "Центральный": "6"},

            "city_zone": {"Москва": ["Измайлово", "Внуково", "Сокольники", "Кунцево", "Крюково", "Лефортово", "Выхино", "Медведково", "Щукино", "Якиманка"],
                          "С. Петербург": ["Центральный", "Невский", "Кировский", "Московский", "Петроградский", "Василеостровской"],
                          "Казань": ["Советский", "Кировский", "Приволжский", "Вахитовский", "Ново-Савиновский", "Московский"],
                          "Екатеринбург": ["Верх-Исетский", "Кировский", "Железнодорожный", "Ленинский", "Октябрьский"],
                          "Сочи": ["Центральный", "Адлерский", "Хостинский", "Лазаревский"],
                          "Краснодар": ["Западный", "Прикубанский", "Карасунский", "Центральный"]},

            "product": {"1": ["Alpha PVP", "Гашиш Euro", "Амфетамин", "Шишки (АК47)", "Мефедрон", "Героин HQ", "Спайс", "Шишко-План"],
                        "2": ["Alpha PVP", "Гашиш Euro", "Амфетамин", "Шишки (АК47)"],
                        "3": ["Alpha PVP", "Гашиш Euro", "Амфетамин", "Мефедрон", "Спайс", "Героин HQ"],
                        "4": ["Alpha PVP", "Гашиш Euro", "Амфетамин", "Мефедрон", "Спайс", "Героин HQ"],
                        "5": ["Alpha PVP", "Гашиш Euro", "Амфетамин", "Спайс"],
                        "6": ["Alpha PVP", "Амфетамин"]},

            "product_price": {"Alpha PVP": ['0.3г (900 руб)', '0.5г (1300 руб)', '1г (2200 руб)', '3г (5500 руб)'],
                              "Гашиш Euro": ['1г (1100 руб)', '2г (2000 руб)', '5г (4000 руб)', '10г (6000 руб)'],
                              "Амфетамин": ['1г (950 руб)', '2г (1800 руб)', '5г (4100 руб)', '10г (6500 руб)'],
                              "Шишки (АК47)": ['1г (1200 руб)', '2г (2200 руб)', '5г (4200 руб)'],
                              "Мефедрон": ['1г (2100 руб)', '2г (4000 руб)', '5г (8000 руб)'],
                              "Героин HQ": ['0.5 (1700 руб)'],
                              "Спайс": ['1г (1200 руб)', '2г (2200 руб)', '5г (4200 руб)'],
                              "Шишко-План": ['1г (550 руб)', '3г (1500 руб)']},

            "price": {'0.3г (900 руб)', '0.5г (1300 руб)', '1г (2200 руб)', '3г (5500 руб)',
                      '1г (1100 руб)', '2г (2000 руб)', '5г (4000 руб)', '10г (6000 руб)',
                      '1г (950 руб)', '2г (1800 руб)', '5г (4100 руб)', '10г (6500 руб)',
                      '1г (1200 руб)', '2г (2200 руб)', '5г (4200 руб)',
                      '1г (2100 руб)', '2г (4000 руб)', '5г (8000 руб)', '0.5 (1700 руб)',
                      '1г (550 руб)', '3г (1500 руб)'}

            } 
