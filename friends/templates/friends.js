var currentUser = current_user
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
    
async function showUsers() {
    try {
        const friendsResponse = await fetch('/get_friends/')
        const currentUser = await friendsResponse.json()

        const usersResponse = await fetch('/get_users_connections/')
        const data = await usersResponse.json()

        users = data.map(user_connection => {
            if (user_connection.user == currentUser.user) return null

            const userCard = userCardTemplate.content.cloneNode(true).children[0]
            const userName = userCard.querySelector("[user-name]")
            const followFollowedButton = userCard.querySelector("[follow-followed-button]")

            userName.textContent = user_connection.user.username

            if (currentUser.friends.includes(user_connection.user.username)) {
                followFollowedButton.textContent = "Followed"
                followFollowedButton.setAttribute("disabled", "true")
            } else {
                followFollowedButton.textContent = "Follow"
                followFollowedButton.addEventListener("click", function () {
                    fetch('/follow_friend/${user_connection.id}', {
                        method: "POST"
                    }).then(refreshFriends)
                })
            }
            userCardsContainer.append(userCard)
            return { name: user_connection.user.username, element: userCard }
        })
    } catch (error) {
        console.error('Error fetching data:', error)
    }
}

showUsers()

async function get_friends() {
    return fetch('/get_friends/').then((response) => response.json())
}

async function refreshFriends() {
    const friends = await get_friends()
    var friendsCount = friends.length
    let friendsCountString = ``
    if (friendsCount == 0) {
        friendsCountString = `You don't have any friends yet`
    } else {
        friends.forEach((friend) => {
            const friendCard = friendCardTemplate.content.cloneNode(true).children[0]
            const friendName = friendCard.querySelector("[friend-name]")
            const seeProfileButton = friendCard.querySelector("[see-profile-button]")
            const unfollowButton = friendCard.querySelector("[unfollow-button]")

            friendName.textContent = friend.user.username

            const profile = profileModal.content.cloneNode(true).children[0]
            const profileName = profile.querySelector("[friend-profile-name]")
            const profileFavorite = profile.querySelector("[friend-favorite]")
            const profileCurrentBook = profile.querySelector("[friend-current-read-book]")

            profileName.textContent = friend.user.username

            //fetch buku yang lagi dibaca user
            //fetch buku yang difavoritin user

            //loop tiap buku si user, trus ubah konten cardnya
            const bookCard = bookCardTemplate.content.cloneNode(true).children[0]
            const bookImg = bookCard.querySelector("[book-img]")
            const bookTitle = bookCard.querySelector("[book-title]")
            

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

