import React from 'react'
import { List } from 'semantic-ui-react'

export const ListResult = ({result}) => {
    return(
        <List className="text-center">
            {result.map(result => {
                return(
                    <List.Item key={result.id}>
                        <List.List>
                            <List.Item>
                                Rank: {result.rank}
                            </List.Item>
                            Link:
                            <List.Item href={result.link}>
                                 {result.link}
                            </List.Item>
                            <List.Item>
                                Relativity: {result.relativity}
                            </List.Item>
                        </List.List>
                        
                    </List.Item>
                )
            })}
        </List>
    )
}