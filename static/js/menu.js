const root = document.getElementById('to-the-main');
const createbook = document.getElementById('createbook');

root.addEventListener('click', () => {
    document.location.pathname = '/';
});
createbook.addEventListener('click', () => {
    document.location.pathname = '/book/create';
});