async function getBooks(genre) {
    return fetch("/searchAndFilters/get_filtered_books/" + genre)
        .then((response) => response.json())
        .then((data) => data);
}

async function getSearchBooks(searchQuery) {
    return fetch("/searchAndFilters/get_search_books/" + searchQuery)
        .then((response) => response.json())
        .then((data) => data);
}

async function searchBooks() {
    var searchQuery = document.getElementById("search-input").value;
    var bookList = document.getElementById("book-list");
    bookList.innerHTML = ""; // Clear the book list
    console.log(searchQuery);

    if (searchQuery) {
        var search = await getSearchBooks(searchQuery);
        console.log(search);

        if (search.length > 0) {
            var container = document.createElement("div");
            container.classList.add("container");

            search.forEach(function (book) {
            var col = document.createElement("div");
    　　　    col.classList.add("col-md-4", "mb-3");
    　　　
    　　　    var card = document.createElement("div");
    　　　    card.classList.add("card");
    　　　
    　　　    var img = document.createElement("img");
    　　　    img.src = book.fields.img;
    　　　    img.classList.add("card-img-top");
    　　　    img.alt = book.fields.title + " Cover";
    　　　
    　　　    var cardBody = document.createElement("div");
    　　　    cardBody.classList.add("card-body");
    　　　
    　　　    var title = document.createElement("h5");
    　　　    title.classList.add("card-title");
    　　　    var titleLink = document.createElement("a");
    　　　    titleLink.href = `/catalog/book_reviews/${book.id}/`;
    　　　    titleLink.textContent = book.fields.title;
    　　　    title.appendChild(titleLink);
    　　　
    　　　    var rating = document.createElement("p");
    　　　    rating.classList.add("card-text");
    　　　    if (book.fields.user_avg_rating) {
    　　　        rating.textContent = "Rating: " + book.fields.user_avg_rating;
    　　　    } else {
    　　　        rating.textContent = "Belum ada rating.";
    　　　    }
    　　　
    　　　    var desc = document.createElement("p");
    　　　    desc.classList.add("card-text");
    　　　    desc.textContent = book.fields.desc;
    　　　
    　　　    var button = document.createElement("button");
    　　　    button.classList.add("btn", "btn-primary", "favorite-button");
    　　　    button.dataset.bookid = book.id;
    　　　    button.textContent = "Tambah ke Favorit";
    　　　
    　　　    cardBody.appendChild(title);
    　　　    cardBody.appendChild(rating);
    　　　    cardBody.appendChild(desc);
    　　　    cardBody.appendChild(button);
    　　　
    　　　    card.appendChild(img);
    　　　    card.appendChild(cardBody);
    　　　
    　　　    col.appendChild(card);
    　　　
    　　　    container.appendChild(col);
    　　　});
    　　　
    　　　bookList.appendChild(container);

            } else {
                bookList.textContent = "No books found for the search query: " + searchQuery;
            }
        }
    }  


async function showBooks() {
    var selectedGenre = document.getElementById("genre-select").value;
    var bookList = document.getElementById("book-list");
    bookList.innerHTML = ""; // Clear the book list

    if (selectedGenre) {
        var books = await getBooks(selectedGenre);
        if (books.length > 0) {
            var container = document.createElement("div");
            container.classList.add("container");

            books.forEach(function (book) {
    　　　    var col = document.createElement("div");
    　　　    col.classList.add("col-md-4", "mb-3");
    　　　
    　　　    var card = document.createElement("div");
    　　　    card.classList.add("card");
    　　　
    　　　    var img = document.createElement("img");
    　　　    img.src = book.fields.img;
    　　　    img.classList.add("card-img-top");
    　　　    img.alt = book.fields.title + " Cover";
    　　　
    　　　    var cardBody = document.createElement("div");
    　　　    cardBody.classList.add("card-body");
    　　　
    　　　    var title = document.createElement("h5");
    　　　    title.classList.add("card-title");
    　　　    var titleLink = document.createElement("a");
    　　　    titleLink.href = `/catalog/book_reviews/${book.id}/`;
    　　　    titleLink.textContent = book.fields.title;
    　　　    title.appendChild(titleLink);
    　　　
    　　　    var rating = document.createElement("p");
    　　　    rating.classList.add("card-text");
    　　　    if (book.fields.user_avg_rating) {
    　　　        rating.textContent = "Rating: " + book.fields.user_avg_rating;
    　　　    } else {
    　　　        rating.textContent = "Belum ada rating.";
    　　　    }
    　　　
    　　　    var desc = document.createElement("p");
    　　　    desc.classList.add("card-text");
    　　　    desc.textContent = book.fields.desc;
    　　　
    　　　    var button = document.createElement("button");
    　　　    button.classList.add("btn", "btn-primary", "favorite-button");
    　　　    button.dataset.bookid = book.id;
    　　　    button.textContent = "Tambah ke Favorit";
    　　　
    　　　    cardBody.appendChild(title);
    　　　    cardBody.appendChild(rating);
    　　　    cardBody.appendChild(desc);
    　　　    cardBody.appendChild(button);
    　　　
    　　　    card.appendChild(img);
    　　　    card.appendChild(cardBody);
    　　　
    　　　    col.appendChild(card);
    　　　
    　　　    container.appendChild(col);
    　　　});
    　　　
    　　　bookList.appendChild(container);
        } else {
            bookList.textContent = "No books found for the selected genre.";
        }
    }
}