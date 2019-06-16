let navSlide = () => {
    let nav = document.getElementById("sidenav");
    let navlinks = document.querySelectorAll(".nav-links li");
    let burger = document.querySelector(".burgers");

    burger.addEventListener("click", () => {
        nav.classList.toggle("sidenav-active");
        nav.style.transition = "all 0.5s";

        navlinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = "";
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 6 + 0.5}s`;
            }
        });
    });
};

navSlide();