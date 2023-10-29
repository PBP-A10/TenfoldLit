fetch("books.json")
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        const bookList = document.getElementById('book-list');
        data.forEach(function (book) {
            const title = book.fields.title;
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.href = `book.html?title=${encodeURIComponent(title)}`;
            link.textContent = title;
            listItem.appendChild(link);
            bookList.appendChild(listItem);
        });
    })
    .catch(function (error) {
        console.error("An error occurred: " + error);
    })