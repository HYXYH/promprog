/**
 * Created by Oskar on 09.03.18.
 */

import React from 'react';



const Task = ({id, text, done, delCallback}) => (

    <li key={id}>
        <form onSubmit={delCallback(id)}>
            <input type="submit" value="Готово"/>
            <label> {text} </label>
        </form>
    </li>
);

export default Task;
