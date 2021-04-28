import './App.css'
import Header from './api/Components/Header'
import Footer from './api/Components/Footer'
import Home from './api/Components/Home'
import Login from './api/Components/Login/Login'
import { BrowserRouter, Route, Routes } from 'react-router-dom'


function App() {
  return (
    <div>
      <BrowserRouter>
          <Header />
            <Routes>
                <Route path="/" element={<Home />} />      
                <Route path="/login" element={<Login />} />      
            </Routes>
          <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
