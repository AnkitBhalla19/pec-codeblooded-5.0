const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const multer = require('multer');
const storage = multer.memoryStorage();
const upload = multer({ dest: 'uploads/' , storage: storage});
const fs = require('fs-extra');
const path = require('path');

app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.post('/upload', upload.single('csvFile'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ message: 'No file uploaded.' });
  }

  const file = req.file;
  const uploadPath = path.join(__dirname, 'uploads', file.originalname);

  // Save the file to the 'uploads/' directory using the standard fs module
  fs.writeFileSync(uploadPath, file.buffer);

  res.json({ message: 'File uploaded and saved successfully.' });
});


app.get('/page2', (req, res) => {
  res.sendFile(__dirname + '/views/page2.html');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
