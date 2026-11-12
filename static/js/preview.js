const STORAGE_KEY = "reportPreview";
const DELAY = 400;

const titleInput = document.getElementById("title");
const descriptionInput = document.getElementById("description");
const toggle = document.getElementById("preview-toggle");
const checkbox = document.getElementById("preview-checkbox");
const preview = document.getElementById("preview");
const previewTitle = document.getElementById("preview-title");
const previewDescription = document.getElementById("preview-description");

let timer = null;

function loadPreference() {
    try {
        const data = JSON.parse(localStorage.getItem(STORAGE_KEY));
        if (data !== null && typeof data === "object" && typeof data.show === "boolean") {
            return data.show;
        }
    } catch (error) {
        console.warn("Could not read preview preference.", error);
    }
    return true;
}

function savePreference(show) {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({ show: show }));
    } catch (error) {
        console.warn("Could not save preview preference.", error);
    }
}

function renderPreview() {
    previewTitle.textContent = titleInput.value.trim();
    previewDescription.textContent = descriptionInput.value.trim();
}

function schedulePreview() {
    clearTimeout(timer);
    if (checkbox.checked) {
        timer = setTimeout(renderPreview, DELAY);
    }
}

function applyState(show) {
    checkbox.checked = show;
    if (show) {
        renderPreview();
        preview.hidden = false;
    } else {
        clearTimeout(timer);
        preview.hidden = true;
    }
}

checkbox.addEventListener("change", function () {
    savePreference(checkbox.checked);
    applyState(checkbox.checked);
});

titleInput.addEventListener("input", schedulePreview);
descriptionInput.addEventListener("input", schedulePreview);

toggle.hidden = false;
applyState(loadPreference());
