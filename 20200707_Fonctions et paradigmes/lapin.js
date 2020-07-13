//niveau1(Hana(a(un(lapin())))) => "Hana a un lapin.)
//niveau2(Le(nom(du(lapin(est(aussi(Hana()))))))) => "Le nom du lapin est aussi Hana."

function lapin() {
  return ".";
}
function un(x) {
  return "lapin" + x;
}
function a(x) {
  return "un " + x;
}
function Hana(x) {
  console.log("Hana a " + x );
}

Hana(a(un(lapin())));
