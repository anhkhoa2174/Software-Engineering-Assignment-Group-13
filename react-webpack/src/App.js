import { Route, Routes } from 'react-router-dom';
import { Fragment, useState } from 'react';
import Navbar from "./components/Navbar/Navbar";
import { routes } from './route';

// Tạo component App
function App() {
    const [element, setElement] = useState('');

    return (
        <div className="app">
            <Navbar handlePage={(val) => setElement(val)} />
            <Routes>
                {routes.map((route, index) => {
                    const Layout = route.layout ? route.layout : Fragment;
                    const Page = route.component;
                    return (
                        <Route
                            key={index}
                            path={route.path}
                            element={
                                <Layout>
                                    <Page />
                                </Layout>
                            }
                        />
                    );
                })}
            </Routes>
        </div>
    );
}

export default App;
// Render component App vào #root element
ReactDOM.render(<App />, document.getElementById("root"));
