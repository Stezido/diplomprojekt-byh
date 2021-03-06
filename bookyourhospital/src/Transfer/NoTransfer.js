import React, { Component } from 'react';
import {Button} from "react-bootstrap";
import history from "../history";
import { withRouter } from 'react-router-dom';


class NoTransfer extends Component{

    render() {
        return (
            <center>
                <div className="KeineUeberweisung" style={{ padding: 30 }}>
                    <Button size={"lg"} variant="dark" onClick={() => history.push('/')}>Zurück zum Start</Button>
                </div>
                <div className="KeineUeberweisung" style={{ padding: 30 }}>
                    <Button size={"lg"} variant="dark" onClick={() => history.push('/WasUeberweisung')}>Was ist eine Überweisung?</Button>
                </div>
            </center>
        );
    }
}
export default withRouter(NoTransfer);