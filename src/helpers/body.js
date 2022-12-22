export const calculateWindowSize = (windowWidth) => {
    if (windowWidth >= 1200) {
        return 'lg';
    }
    if (windowWidth >= 992) {
        return 'md';
    }
    if (windowWidth >= 768) {
        return 'sm';
    }
    return 'xs';
};

export const addWindowClass = (classList) => {
    const window = document.body
    if (window) {
      window.classList.add(classList);
    }
}

export const removeWindowClass = (classList) => {
    const window = document.body
    if (window) {
      window.classList.remove(classList);
    }
}