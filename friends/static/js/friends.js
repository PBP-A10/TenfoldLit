const userCardTemplate = document.querySelector("[user-card-template]")
const userCardsContainer = document.querySelector("[users-card-container]")
const searchInput = document.querySelector("[data-search]")

const friendCardTemplate = document.querySelector("[friend-card-template]")
const friendCardsContainer = document.querySelector("[main-container]")

const profileModal = document.querySelector("[friend-profile-modal]")

const bookCardTemplate = document.querySelector("[book-card-template]")

let users = []

searchInput.addEventListener("input", (e) => {
    const value = e.target.value.toLowerCase()
    users.forEach(user => {
        if (user == null) {return}
        const isVisible = user.username.toLowerCase().includes(value)
        user.element.classList.toggle("hide", !isVisible)
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
        console.log(usersResponse)

        const currentUserFriends = currentUser[0].fields.friends
        users = usersResponse.map(async user_connection => {
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
            return { name: user_connection.fields.user.username, element: userCard }
        })
    } catch (error) {
        console.error('Error fetching data:', error)
    }
}

const openSearchModalButton = document.getElementById("open-search-modal")
openSearchModalButton.addEventListener("click", showUsers)

const searchModal = document.getElementById("searchModal")
searchModal.addEventListener("hidden.bs.modal", function() {
    userCardsContainer.innerHTML = ""
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

            console.log(userConnection[0].fields.user)
            const user = await getUser(userConnection[0].fields.user)
            console.log(user)
            friendName.textContent = user[0].fields.username

            const profile = profileModal.content.cloneNode(true).children[0]
            const profileName = profile.querySelector("[friend-profile-name]")
            const profileFavorite = profile.querySelector("[friend-favorite]")
            const profileCurrentBook = profile.querySelector("[friend-current-read-book]")

            profileName.textContent = user[0].fields.username

            //fetch buku yang lagi dibaca user

            //fetch buku yang difavoritin user

            //loop tiap buku yang lagi dibaca si user, trus ubah konten cardnya
            const bookCard = bookCardTemplate.content.cloneNode(true).children[0]
            const bookImg = bookCard.querySelector("[book-img]")
            const bookTitle = bookCard.querySelector("[book-title]")
            
            //loop tiap buku yang difavoritin si user, trus ubah konten cardnya

            seeProfileButton.addEventListener("click", function () {
                new bootstrap.modal(profile).show()
            })

            unfollowButton.addEventListener("click", function () {
                fetch('/unfollow_friends/${friend.id}').then(refreshFriends)
            })

            friendCardsContainer.append(friendCard)
        })
    }
}

refreshFriends()

