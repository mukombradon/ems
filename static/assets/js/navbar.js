function toggleDropdown() {
    const menu = document.getElementById("dropdownMenu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

// Optional: Close dropdown if clicking outside
document.addEventListener("click", function(event) {
    const profileIcon = document.querySelector(".profile-icon");
    const dropdownMenu = document.getElementById("dropdownMenu");

    if (!profileIcon.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.style.display = "none";
    }
});
