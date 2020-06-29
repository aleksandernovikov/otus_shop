# Graduation Project "Online Store" in Otus
#### Uses:
 - Organi template on Bootstrap 4.x
 - Jquery 3.x
 - Django 3.x, Django Rest Framework
 - Any database supported by Django


#### Opportunities:

 - Nice responsive design 
 - SEO Friendly
 - Showcase of products with categories with the ability to sort
 - Product Sales Ad Unit
 - The ability to add an infinite number of product characteristics
 - The ability to add an infinite number of product images
 - Selling price and crossed out price of product
 - Cart of products
 - View Order History
 - The ability to add products to favorites
 - The presence of a blog for posting articles and news
 - User profile with avatar
 - Ability to subscribe to shop newsletters
 - The ability to write a message to the shop administrator
 - The ability to conveniently configure basic information about the shop
 
# Installation instruction
 - Clone repository `git clone https://github.com/aleksandernovikov/otus_shop.git`
 - Install Dependencies `cd otus-shop && pip install -r requirements.txt`
 - Make migrations `python manage.py migrate`
 - To fill in demo data, call the `python manage.py populate` command
 
# Docker
Run command in project root `docker build -t otus-shop . && docker run -p 8000:8000 -t otus-shop`

# Todo
- [x] страницу профиля пользователя
- [x] страницу заказов пользователя
- [x] страницу выхода
- [x] блок распродаж
- [x] подписка на новости
- [x] сообщение со страницы контактов
- [x] favorites, страница favorites
- [x] добавить характеристики продукта
- [ ] блок рекомендованных продуктов внизу страницы товара
- [ ] гамбургер
- [ ] На главной рекомендованные продукты
- [ ] поиск
- [ ] фильтр товаров
- [ ] вынести бизнес логику
- [ ] описать модели и вьюхи
