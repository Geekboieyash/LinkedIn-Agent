import Header from './components/Header';
import Footer from './components/Footer';
import PostGenerator from './components/PostGenerator';
import './index.css';

const App = () => {
  return (
    <div className="page-div">
      <Header />
      <main className="content-div">
        <PostGenerator />
      </main>
      <Footer />
    </div>
  );
};

export default App;