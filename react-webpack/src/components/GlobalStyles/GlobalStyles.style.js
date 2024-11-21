import { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`

  @import url('//fonts.googleapis.com/css2?family=Unbounded');

  *, *::after, *::before {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  :root {
    //color
    --boundedFont: 'Unbounded', sans-serif;
    --super-text_size: 52px;
    --primary-text_size: 40px;
    --title-text_size: 32px;
    --large-text_size: 24px;
    --medium-text_size: 20px;
    --normal-text_size: 16px;
    //fontWeight: 
    --small-fontWeight: 400;
    --normal-fontWeight: 600;
    --large-fontWeight: 800;
    --XL-fontWeight: 900;
  }

  html {
    height: 100%;
    .app {
      width: 100%;
    }
  }

  body {
    font-size: 1.6rem;
    line-height: 1.5;
    min-height: 100vh; 
    text-rendering: optimizeSpeed;
    background-color: #ffffff;
  }

  #root {
    display: flex;
  }
`;

export default GlobalStyles;
