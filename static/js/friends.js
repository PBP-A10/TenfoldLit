const userCardTemplate = document.querySelector("[user-card-template]")
const userCardsContainer = document.querySelector("[users-card-container]")
const searchInput = document.querySelector("[data-search]")

const friendCardTemplate = document.querySelector("[friend-card-template]")
const friendCardsContainer = document.querySelector("[main-container]")

const bookCardTemplate = document.querySelector("[book-card-template]")

const friendFavoriteContainer = document.querySelector("[carousel]")
const friendCurrentReadBookContainer = document.querySelector("[friend-current-read-book]")
const friendProfileName = document.querySelector("[friend-profile-name]")

let users = []

searchInput.addEventListener("input", (e) => {
    const value = e.target.value.toLowerCase()
    users.forEach(user => {
        if (user == null) {return}
        const isVisible = user.name.toLowerCase().includes(value)
        if (!isVisible) {
            user.element.style.display = "none"
        } else {
            user.element.style.display = "block"
        }
    })
})

async function getFriends() {
    return fetch(url_get_friends).then((response) => response.json()).then((data) => data)
}

async function getAllUserConnections() {
    return fetch(url_get_all_user_connections).then((response) => response.json()).then((data) => data)
}

async function getUser(user_id) {
    return fetch(url_get_user.replace(/1/, user_id)).then((response) => response.json()).then((data) => data)
}
    
async function showUsers() {
    try {
        const currentUser = await getFriends()

        const usersResponse = await getAllUserConnections()

        const currentUserFriends = currentUser[0].fields.friends
        users = await Promise.all(usersResponse.map(async user_connection => {
            if (user_connection.pk == currentUser[0].pk) return null

            const userCard = userCardTemplate.content.cloneNode(true).children[0]
            const userName = userCard.querySelector("[user-name]")
            const followFollowedButton = userCard.querySelector("[follow-followed-button]")
            
            const user = await getUser(user_connection.fields.user)
            userName.textContent = user[0].fields.username

            if (currentUserFriends.includes(user_connection.pk)) {
                followFollowedButton.textContent = "Followed"
                followFollowedButton.classList.remove("btn-primary")
                followFollowedButton.classList.add("btn-secondary")
                followFollowedButton.setAttribute("disabled", "true")
            } else {
                followFollowedButton.textContent = "Follow"
                followFollowedButton.addEventListener("click", function () {
                    fetch(url_follow_friend.replace(/1/, user_connection.pk), {
                        method: "POST",
                        headers: {
                            'X-CSRFToken': csrfToken
                        }
                    }).then(refreshFriends)
                    followFollowedButton.classList.remove("btn-primary")
                    followFollowedButton.classList.add("btn-secondary")
                    followFollowedButton.setAttribute("disabled", "true")
                    followFollowedButton.textContent = "followed"
                })
            }
            userCardsContainer.append(userCard)
            return { name: user[0].fields.username, element: userCard }
        }))
    } catch (error) {
        console.error('Error fetching data:', error)
    }
}

const openSearchModalButton = document.getElementById("open-search-modal")
openSearchModalButton.addEventListener("click", showUsers)

const searchModal = document.getElementById("searchModal")
searchModal.addEventListener("hidden.bs.modal", function() {
    userCardsContainer.innerHTML = ""
    searchInput.value = ""
})

async function getUserConnections(user_id) {
    return fetch(url_get_user_connections.replace(/1/, user_id)).then((response) => response.json()).then((data) => data)
}

async function refreshFriends() {
    friendCardsContainer.innerHTML = ""
    const currentUserFriends = await getFriends()
    var friendsCount = currentUserFriends.length
    let friendsCountString = ``
    if (friendsCount == 0) {
        friendsCountString = `You don't have any friends yet`
    } else {
        currentUserFriends[0].fields.friends.forEach(async (friend) => {
            const friendCard = friendCardTemplate.content.cloneNode(true).children[0]
            const friendName = friendCard.querySelector("[friend-name]")
            const seeProfileButton = friendCard.querySelector("[see-profile-button]")
            const unfollowButton = friendCard.querySelector("[unfollow-button]")
            const userConnection = await getUserConnections(friend)

            const user = await getUser(userConnection[0].fields.user)
            friendName.textContent = user[0].fields.username

            //loop tiap buku yang lagi dibaca si user, trus ubah konten cardnya
            const bookCard = bookCardTemplate.content.cloneNode(true).children[0]
            const bookImg = bookCard.querySelector("[book-img]")
            const bookTitle = bookCard.querySelector("[book-title]")
            
            //loop tiap buku yang difavoritin si user, trus ubah konten cardnya

            seeProfileButton.addEventListener("click", function () {
                seeProfile(user)
            })

            unfollowButton.addEventListener("click", function () {
                fetch(url_unfollow_friend.replace(/1/, userConnection[0].pk), {
                    method: "POST",
                    headers: {
                        'X-CSRFToken': csrfToken
                    }
                }).then(refreshFriends)
            })

            friendCardsContainer.append(friendCard)
        })
    }
}

refreshFriends()

async function getBorrowedBooks(user_id) {
    return fetch(url_get_borrowed_books.replace(/1/, user_id)).then((response) => response.json()).then((data) => data)
}

async function getFavoriteBooks(user_id) {
    return fetch(url_get_favorite_books.replace(/1/, user_id)).then((response) => response.json()).then((data) => data)
}

async function seeProfile(user) {
    //fetch buku favorite user

    //fetch buku yang lagi dibaca user
    friendProfileName.textContent = user[0].fields.username
    const borrowedBooks = await getBorrowedBooks(user[0].pk)
    const favoriteBooks = await getFavoriteBooks(user[0].pk)

    if (borrowedBooks.length == 0) {
        friendFavoriteContainer.textContent = "Your friend doesn't have a favorite book yet"
    } else {
        favoriteBooks.forEach((book) => {
            const bookCard = bookCardTemplate.content.cloneNode(true).children[0]
            const bookImg = bookCard.querySelector("[book-img]")
            const bookTitle = bookCard.querySelector("[book-title]")
            bookImg.setAttribute('src', book.fields.img)
            bookTitle.textContent = book.fields.title
            friendFavoriteContainer.append(bookCard)
        })
    }

    if (favoriteBooks.length == 0) {
        friendCurrentReadBookContainer.textContent = "Your friend isn't reading any books"
    } else {
        borrowedBooks.forEach((book) => {
            const bookCard = bookCardTemplate.content.cloneNode(true).children[0]
            const bookImg = bookCard.querySelector("[book-img]")
            const bookTitle = bookCard.querySelector("[book-title]")
            bookImg.setAttribute('src', book.fields.img)
            bookTitle.textContent = book.fields.title
            friendCurrentReadBookContainer.append(bookCard)
        })
    }
}

const profileModal = document.getElementById("seeProfile")
profileModal.addEventListener("hidden.bs.modal", function() {
    friendFavoriteContainer.innerHTML = ""
    friendCurrentReadBookContainer.innerHTML = ""
})