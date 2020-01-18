export const showError = msg => {
  let error = document.getElementById("error-alert");
  error.innerHTML = msg;
  error.style.top = "20px";
  setTimeout(() => {
    error.style.top = "-100px";
  }, 5000);
};
