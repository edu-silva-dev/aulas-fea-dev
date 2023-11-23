let numeroDasorte = [34 , 14 , 26 , 594 , 47]
for(let i =0; i< numeroDasorte.length;i++){
    if (numeroDasorte[i] % 2 ==0 && numeroDasorte[i] <= 50){
        console.log('Numeros menores que 50 que são pares =', numeroDasorte[i])
    }
else if (numeroDasorte[i] != 0 && numeroDasorte[i] <= 50){
    console.log('Numeros menores que 50 que não são pares =', numeroDasorte[i])
}
}



