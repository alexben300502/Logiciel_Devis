import streamlit as st

# Fonction appelée pour récupérer les informations
def recuperer_informations(rideaux, hauteur, type_tringle, type_confection, ampleur):
    if rideaux and hauteur and type_tringle and type_confection and ampleur:
        # Remplir les champs avec des valeurs simulées pour le calcul
        tarif_confection = "Calculé"
        tarif_tringle = "Calculé"
        tarif_tissu = "Calculé"
        quantite_tissu = "Calculé"
        return tarif_confection, tarif_tringle, tarif_tissu, quantite_tissu
    else:
        st.warning("Veuillez remplir tous les champs pour obtenir les tarifs.")
        return None, None, None, None

# Titre de l'application
st.title("LOGICIEL")

# Champs de saisie pour les informations de rideaux
rideaux = st.text_input("Largeur rideaux (en m) :")
hauteur = st.text_input("Hauteur rideaux (en m) :")

# Sélection pour le type de tringle
type_tringle = st.selectbox("Type de tringle :", ["", "A", "B", "C"])

# Sélection pour le type de confection
type_confection = st.selectbox("Type de confection :", ["", "E", "F", "G"])

# Sélection pour l'ampleur
ampleur = st.selectbox("Ampleur :", ["", "1,50", "2", "2,50"])

# Bouton pour valider les informations et calculer les tarifs
if st.button("Valider"):
    # Récupérer et afficher les résultats
    tarif_confection, tarif_tringle, tarif_tissu, quantite_tissu = recuperer_informations(
        rideaux, hauteur, type_tringle, type_confection, ampleur
    )
    
    if tarif_confection and tarif_tringle and tarif_tissu and quantite_tissu:
        st.subheader("Résultats")
        st.write(f"Tarif vente confection : {tarif_confection}")
        st.write(f"Tarif tringle : {tarif_tringle}")
        st.write(f"Tarif vente tissus : {tarif_tissu}")
        st.write(f"Quantité tissu : {quantite_tissu}")
