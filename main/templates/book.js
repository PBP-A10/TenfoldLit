// const urlParams = new URLSearchParams(window.location.search);
// const title = urlParams.get("title");

// fetch("books.json") // Assuming the JSON file is named "books.json"
//     .then(function (response) {
//         return response.json();
//     })
//     .then(function (data) {
//         const bookDetails = document.getElementById('book-details');
//         const book = data.find(book => book.fields.title === title);
//         if (book) {
//             const fields = book.fields;

//             // Create and populate linear book detail elements
//             const titleElement = document.createElement('h2');
//             titleElement.textContent = fields.title;
//             bookDetails.appendChild(titleElement);

//             const authorElement = document.createElement('p');
//             authorElement.textContent = `Author: ${fields.author}`;
//             bookDetails.appendChild(authorElement);

//             const bookFormatElement = document.createElement('p');
//             bookFormatElement.textContent = `Book Format: ${fields.bookformat}`;
//             bookDetails.appendChild(bookFormatElement);

//             const descElement = document.createElement('p');
//             descElement.textContent = `Description: ${fields.desc}`;
//             bookDetails.appendChild(descElement);

//             const genreElement = document.createElement('p');
//             genreElement.textContent = `Genre: ${fields.genre}`;
//             bookDetails.appendChild(genreElement);

//             const isbnElement = document.createElement('p');
//             isbnElement.textContent = `ISBN: ${fields.isbn}`;
//             bookDetails.appendChild(isbnElement);

//             const isbn13Element = document.createElement('p');
//             isbn13Element.textContent = `ISBN13: ${fields.isbn13}`;
//             bookDetails.appendChild(isbn13Element);

//             const pagesElement = document.createElement('p');
//             pagesElement.textContent = `Pages: ${fields.pages}`;
//             bookDetails.appendChild(pagesElement);

//             const ratingElement = document.createElement('p');
//             ratingElement.textContent = `Rating: ${fields.rating}`;
//             bookDetails.appendChild(ratingElement);

//             const reviewsElement = document.createElement('p');
//             reviewsElement.textContent = `Reviews: ${fields.reviews}`;
//             bookDetails.appendChild(reviewsElement);
//         } else {
//             bookDetails.textContent = "Book not found";
//         }
//     })
//     .catch(function (error) {
//         console.error("An error occurred: " + error);
//     });
