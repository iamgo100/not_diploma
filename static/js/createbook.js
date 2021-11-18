const form = document.querySelector('form');
const readyBtn = document.getElementById('ready');
const cancelBtn = document.getElementById('cancel');

const authorSelect = form.elements['author-select'];
const author = document.getElementById('author');

const pOfficeSelect = form.elements['p_office-select'];
const pOffice = document.getElementById('p_office');

const seriesSelect = form.elements['series-select'];
const series = document.getElementById('series');
const part = document.getElementById('part');

const belongF = document.getElementById('belongF');
const radioFilm = form.elements['belong-film'];
const filmEl = document.getElementById('film');

const checking = (selector, value, hiddenEl) => { // проверяем, нужно прятать или показывать определенный элемент
    console.log(selector.value, value)
    if (selector.value === value) {
        hiddenEl.classList.remove('hidden')
    } else {
        hiddenEl.classList.add('hidden')
    };
};

const selecting = (selector, value, hiddenEl) => { // работа с селекторами
    selector.childNodes.forEach((el) => {           // ставим нужную опцию
        if (el.value === selector.dataset.value) {
            el.selected = true
        };
    });
    selector.addEventListener('change', () => { // на изменение селектора вызываем функцию проверки, чтобы спрятать или показать элемент
        console.log(selector, 'changed')
        checking(selector, value, hiddenEl)
    });
};

selecting(authorSelect, 'Новый автор', author);
checking(authorSelect, 'Новый автор', author);

selecting(pOfficeSelect, 'Новое издательство', pOffice);
checking(pOfficeSelect, 'Новое издательство', pOffice);

selecting(seriesSelect, 'Новая серия', series);
checking(seriesSelect, 'Новая серия', series);

// работа с проверками и событиями для элемента part из документа html
// подобно тому, что есть выше
if (seriesSelect.value !== 'Выберите серию' && seriesSelect.value !== 'Нет серии') {
    part.classList.remove('hidden')
} else {
    part.classList.add('hidden')
};
seriesSelect.addEventListener('change', () => {
    if (seriesSelect.value !== 'Выберите серию' && seriesSelect.value !== 'Нет серии') {
        part.classList.remove('hidden')
    } else {
        part.classList.add('hidden')
    };
});

// работа с проверками и событиями для элемента film-adapt из документа html
// подобно тому, что есть выше
radioFilm[0].addEventListener('change', () => {
    if (radioFilm[0].checked) {
        filmEl.classList.remove('hidden');
    };
});
radioFilm[1].addEventListener('change', () => {
    if (radioFilm[1].checked) {
        filmEl.classList.add('hidden');
    };
});
if (belongF.dataset.value.toString() === "true") {
    radioFilm[0].checked = true
};
if (belongF.dataset.value.toString() === "false") {
    radioFilm[1].checked = true
};
if (radioFilm[0].checked) {
    filmEl.classList.remove('hidden');
};
if (radioFilm[1].checked) {
    filmEl.classList.add('hidden');
};

// обработка событий для кнопок
// кнопка "Готово" - отправка формы на сервер
readyBtn.addEventListener('click', () => {
    form.submit();
});

// кнопка "Отмена" - возврат на главную страницу без отправки и сохранения формы
cancelBtn.addEventListener('click', () => {
    document.location.pathname = '/';
});