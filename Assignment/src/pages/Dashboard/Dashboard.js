import React from 'react';
import styled from 'styled-components';
export const DashboardLayout = styled.div`
    width: 100%;
    padding: 0 5%;
    display: flex;
    flex-direction: column;
`;

export default function Dashboard() {
    return (
        <DashboardLayout>  
            <div
                style={{
                    width: "551px",
                    height: "149px",
                    left: "966px",
                    top: "166.3px",
                    position: "absolute",
                    background: "white",
                    boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
                    border: "1px #d8d8d8 solid"
                }}></div>
            <div
                style={{
                    width: "551px",
                    height: "149px",
                    left: "966px",
                    top: "343.3px",
                    position: "absolute",
                    background: "white",
                    boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
                    border: "1px #d8d8d8 solid"
                }}></div>
            <div
                style={{
                    width: "551px",
                    height: "149px",
                    left: "966px",
                    top: "522.3px",
                    position: "absolute",
                    background: "white",
                    boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
                    border: "1px #d8d8d8 solid"
                }}></div>
            
            
        </DashboardLayout>
    );
}
