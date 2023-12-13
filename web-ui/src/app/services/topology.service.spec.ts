import { TestBed } from '@angular/core/testing';

import { TopologyService } from './topology.service';

describe('TopologyService', () => {
  let service: TopologyService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TopologyService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
