/* Client-side validation for the Emotion Detector form. */
"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("emotion-form");
    const input = document.getElementById("feedback");
    const error = document.getElementById("client-error");

    form.addEventListener("submit", (event) => {
        if (!input.value.trim()) {
            event.preventDefault();
            error.hidden = false;
            input.focus();
            return;
        }
        error.hidden = true;
    });

    input.addEventListener("input", () => {
        if (input.value.trim()) {
            error.hidden = true;
        }
    });
});
