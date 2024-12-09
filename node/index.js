const express = require('express');
const app = express();
const port = 3000;

// Middleware para interpretar JSON no corpo da requisição
app.use(express.json());

// Array de produtos
const products = [
    { id: 1, name: 'Notebook', price: 2500 },
    { id: 2, name: 'Smartphone', price: 1500 }
];

// Rota GET para listar produtos
app.get('/products', (req, res) => {
    res.json(products);
});

// Rota POST para adicionar novos produtos
app.post('/products', (req, res) => {
    const { name, price } = req.body;

    // Validação básica para verificar se os campos foram enviados
    if (!name || !price) {
        return res.status(400).json({ error: 'Nome e preço são obrigatórios' });
    }

    const newProduct = {
        id: products.length + 1, // Gera um novo ID
        name,
        price
    };

    products.push(newProduct); // Adiciona o novo produto ao array
    res.status(201).json(newProduct); // Retorna o novo produto criado
});

// Inicia o servidor
app.listen(port, () => {
    console.log(`API is running on http://localhost:${port}`);
});
