
import Error404 from "@container/errors/Error404";
import Home from "@container/pages/Home";
import { Provider } from "react-redux";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import store from "./store";

function App() {
  return (

    <Provider store={store}>
      <Router>
        <Routes>
          <Route path="*" element={<Error404 />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </Router>

    </Provider>




  );
}

export default App;
