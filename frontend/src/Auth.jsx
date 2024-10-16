function CheckToken() {
  const token = localStorage.getItem("token");

  return !(
    token === "undefined" ||
    token === "" ||
    token === undefined ||
    token === null
  );
}

export default CheckToken;
