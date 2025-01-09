export function getCSRFToken() {
  const match = document.cookie.match(/csrf_token=([^;]+)/);
  console.log("Retrieved CSRF Token:", match ? match[1] : "None Found");
  return match ? match[1] : null;
}
