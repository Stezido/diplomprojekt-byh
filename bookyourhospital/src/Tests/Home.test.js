import React from 'react';
import ReactDOM from 'react-dom';
import { act } from 'react-dom/test-utils';
import Home from "../Home/Home";

let container;

beforeEach(() => {
    container = document.createElement('div');
    document.body.appendChild(container);
});

afterEach(() => {
    document.body.removeChild(container);
    container = null;
});

it('Home: can render and select a button', () => {
    // Test first render and componentDidMount
    act(() => {
        ReactDOM.render(<Home />, container);
    });

    //get elements and set values
    const button = container.querySelector('button');
    //const input = container.querySelector('input');
    //input.value = "34565";

    //simulate click
    act(() => {
        button.dispatchEvent(new MouseEvent('click', {bubbles: true}));
    });
});

