const annotationText = document.getElementById('annot-text');
const filmAdaptText = document.getElementById('film-text');

const setText = (cont, text) => {
    cont.innerHTML = `${text}`;
};

if (annotationText) setText(annotationText, annotationText.textContent)
if (filmAdaptText) setText(filmAdaptText, filmAdaptText.textContent)