export function isEmpty(value) {
    return value === null || value === undefined || value.trim() === '';
}

export function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/* export function isValidPassword(password) {
    return password.length >= 3;
} */