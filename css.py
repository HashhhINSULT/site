body {
    font-family: Helvetica; /* Семейство шрифтов */
    font-size: 14px; /* Размер основного шрифта в <p></p>  */
    background-color: #000000; /* Цвет фона веб-страницы */
    color: #d4d4d4; /* Цвет основного текста */ 
}
h1 {
    color: hsl(187, 85%, 71%); /* Цвет заголовка */
    font-size: 24px; /* Размер шрифта в пунктах */
    font-family: Georgia, serif; /* Семейство шрифтов */
}

@keyframes color-change {
    0% {
      color: rgb(101, 226, 237);
    }
  
    20% {
      color: rgb(114, 173, 193);
    }
  
    40% {
      color: rgb(65, 121, 134);
    }

    60% {
      color: rgb(54, 85, 89);
    }

    80% {
      color: rgb(100, 155, 171);
    }

    100% {
      color: rgba(138, 237, 232, 0.863);
    }
}

h1 {
    animation: color-change 3s infinite;
}
