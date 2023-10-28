<style>
  *{
    box-sizing: border-box;
    padding: 0;
    margin: 0;
  }
  html{
    margin: 0;
    padding: 0;
  }
  body{
    background-color:#232323;
    margin: 0;
    padding: 0;
  }
  .zagolovok{
    font-size: 50px;
    text-align: center;
    Color: #eeeeee;
    line-height: 60px;
    background-color: #303030;
    padding: 10px;
    border-radius: 10px;
    transition: background-color 1s ease;
    margin: 20px;
  }

  .zagolovok:hover{
    background-color: #363636;
  }

  .zag__mini{
    font-size: 30px;
    Color: #eeeeee;
    margin: 20px;
    margin-top: 50px
  }

  .mini-info{
    background-color: #303030;
    Color: #eeeeee;
    margin: 20px;
    padding: 10px;
    border: dashed 4px #eeeeee;
    font-size: 15px;
    border-radius: 10px;
  }

  .mini-info2{

    Color: #eeeeee;
    margin: 10px;
    padding: 10px;
    font-size: 20px;
    border-radius: 10px;
  }

  .listitem{
    Color: #eeeeee;
    margin: 20px;
    font-size: 15px;

  }

  .instruct{
    Color: #eeeeee;
    text-align: center;
    font-size: 30px;
    margin: 20px;
    margin-top: 50px;
  }
  .container{
    display: flex;
    align-items: center;
    justify-content: space-evenly;
  }

  .item{
    background-color: #303030;
    Color: #eeeeee;
    font-size: 20px;
    border-radius: 10px;
    padding: 20px;
    width: calc(50% - 40px);
    height: 200px;
    display: flex;
    justify-content:center;
    align-items:center;
    text-align: center;
  }
  .members{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .members__item{
    width: calc(50vw - 40px);
    background-color: #303030;
    color: #eeeeee;
    font-size: 20px;
    padding:10px;
    border-radius: 10px;
    text-align: center;
  }
  .tg{
    width: 100px;
    margin: 10px;
  }
</style>


<div class = "zagolovok">Программа для подсчёта ТБО на видео.</div>


<h3 class="zag__mini">-Краткая информация</h3>

<p class="mini-info">Данная программа решает проблему подсчёта количества <a href = "https://ru.wikipedia.org/wiki/%D0%A2%D0%B2%D1%91%D1%80%D0%B4%D1%8B%D0%B5_%D0%B1%D1%8B%D1%82%D0%BE%D0%B2%D1%8B%D0%B5_%D0%BE%D1%82%D1%85%D0%BE%D0%B4%D1%8B">ТБО</a> на видео при помощи модели V8s фреймворка<a href="https://github.com/ultralytics/ultralytics">  Yolo</a> и самописных алгоритмов.</p>

<h3 class="zag__mini">-Основные возможности</h3>

<p class="mini-info2">На вход подаются <strong>фреймы</strong> видео (снимки).</p>
<p class="mini-info2">
На выходе вы получаете следующие <strong>файлы:</strong></p>

  <p class="listitem">1)Количество каждого типа ТБО (дерево, пластик, стекло металл) на протяжении всего видео.</p>
  <p class="listitem">
  2)Количество каждого типа ТБО (дерево, пластик, стекло металл) на кокнретном фрейме (снимке).</p>

  <h3 class="instruct">
Инструкция по установке/подключению</h3>


<h3 class="instruct">Инструкция по запуску в режиме разработчика и в режиме пользователя
Для разработчиков:</h3>

<div class="container">
<div class="item">Склонировать репозиторий github</div>
<div class="item">Настроить параметры под нужды</div>
</div>



  <h3 class="instruct">
Для пользователя:</h3>

<div class="container">
<div class="item">Скачать exe версию продукта</div>
<div class="item">Запустить и настроить</div>
</div>

<h3 class="instruct">Участники проекта</h3>
<div class="members">

  <p class="members__item">Дмитрий </br><a href="https://www.t.me/sekrittt"><img class="tg" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/800px-Telegram_logo.svg.png"></a></p>
  <p class="members__item">Денис </br><a href="https://www.t.me/deniisus"><img class="tg" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/800px-Telegram_logo.svg.png"></a></p>
  <p class="members__item">Захар </br><a href="https://www.t.me/misericors"><img class="tg" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/800px-Telegram_logo.svg.png"></a></p>
  <p class="members__item">Никита </br><a href="https://www.t.me/Sample007"><img class="tg" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/800px-Telegram_logo.svg.png"></a></p>
</div>
