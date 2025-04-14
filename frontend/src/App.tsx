import Header from './components/Header';
import Footer from './components/Footer';
import PostGenerator from './components/PostGenerator';

const App = () => {
  return (
    <div className="min-h-screen flex flex-col bg-[#f2f4f8]">
      <Header />
      <main className="flex-1 p-6">
        <PostGenerator />
      </main>
      <Footer />
    </div>
  );
};

export default App;
